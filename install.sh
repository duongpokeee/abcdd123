#!/bin/bash

# Cập nhật danh sách gói
sudo yes | apt update

# Cài đặt screen
sudo yes | apt install screen

# Tạo một session screen có tên "testapp"
screen -dmS testapp bash -c '
  git clone https://github.com/duongpokeee/abcdxyz2 && 
  cd abcdxyz2 && 
  node app.js
