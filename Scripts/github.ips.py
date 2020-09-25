import requests
import re
import os
from netaddr import IPNetwork


def is_overlap(old, new):
    old_net = IPNetwork(old)
    new_net = IPNetwork(new)
    return old_net in new_net


def write_to_file(content):
    root_path = os.path.abspath(os.path.dirname(os.getcwd()))
    surge_path = root_path + "/Surge/Provider/Github.IPs.list"
    clash_path = root_path + "/Clash/Provider/Github.IPs"

    # Surge
    file = open(surge_path, "w")
    for i, item in enumerate(content):
        file.write("IP-CIDR," + item + ",no-resolve")
        if i != len(content) - 1:
            file.write("\n")
    file.close()

    # Clash
    file = open(clash_path, "w")
    file.write("payload:\n")
    for i, item in enumerate(content):
        file.write("    - '" + item + "'")
        if i != len(content) - 1:
            file.write("\n")
    file.close()

if __name__ == '__main__':
    url = "https://api.github.com/meta"
    req = requests.get(url)
    response = req.json()

    hooks = response['hooks']
    web = response['web']
    api = response['api']
    git = response['git']
    pages = response['pages']
    importer = response['importer']

    combination = list(set(hooks + web + api + git + pages + importer))
    cidr = []
    ips = []

    for item in combination:
        ip = IPNetwork(item)
        if ip.size > 1:
            cidr.append(item)
        else:
            ips.append(item)

    result = []
    index = 0
    for i in cidr:
        tmp = []
        for j in ips:
            if is_overlap(j, i) is False:
                tmp.append(j)
        ips = tmp
        index += 1
        if index == len(cidr) - 1:
            result = ips

    result = list(set(result + cidr))
    result = sorted(result, key=lambda x: [int(m)
                                           for m in re.findall("\\d+", x)])
    write_to_file(result)