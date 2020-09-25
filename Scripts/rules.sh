#!/bin/bash

current_directory=$(cd "$(dirname "$0")";pwd) || return
parent_directory=$(dirname "$current_directory")

export http_proxy=http://127.0.0.1:8118
export https_proxy=http://127.0.0.1:8118
export all_proxy=socks5://127.0.0.1:1080

github() {
    cd "$current_directory" || return
    github_script_path="$current_directory/github.ips.py"
    python3 "$github_script_path"
    cd "$parent_directory" || return
    git add .
    git commit -m "Github IPs Update"
    git push
}

github

unset http_proxy
unset https_proxy
unset all_proxy
