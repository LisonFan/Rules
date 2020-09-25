#!/bin/bash

current_directory="$PWD"
parent_directory=$(dirname "$PWD")

export http_proxy=http://127.0.0.1:8118
export https_proxy=http://127.0.0.1:8118
export all_proxy=socks5://127.0.0.1:1080

github() {
    github_script_path="$current_directory/github.ips.py"
    python "$github_script_path"
    cd "$parent_directory" || return
    git add .
    git commit -m "Github IPs Update"
    git push
}

github
