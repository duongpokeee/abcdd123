#!/bin/bash

# Cập nhật danh sách gói
sudo apt update -y
apt update -y
# Cài đặt screen
sudo apt install -y screen
apt install -y screen
# Tạo một phiên screen mới có tên "testapp"
screen -dmS testapp bash -c "
    git clone https://github.com/duongpokeee/abcdxyz2 &&
    cd abcdxyz2 &&
    node app.js
"
