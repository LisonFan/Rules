import requests
import re
import os



if __name__ == '__main__':
    url = "https://github.com/Hackl0us/GeoIP2-CN/raw/release/CN-ip-cidr.txt"
    req = requests.get(url, proxies = {'https': 'http://127.0.0.1:8118'})
    response = req.text
    china_ip_arr = response.split('\n')
    
    root_path = os.path.abspath(os.path.dirname(os.getcwd()))
    clash_path = root_path + "/Clash/Provider/China.IPs"
    # Clash
    file = open(clash_path, "w")
    file.write("payload:\n")
    for i, item in enumerate(china_ip_arr):
        if len(item) > 0 and item.isspace() == False:
            file.write("    - '" + item + "'")
            if i != len(china_ip_arr) - 1:
                file.write("\n")
    file.close()