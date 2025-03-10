import requests
from datetime import datetime
from time import sleep
import os

TOKEN = '6996163606:AAEKw639tINrZJRmoy6-kCjmVZ-UMHgV7go'
CHAT_ID = '-4207787304'

# MY_MESSAGE_TEXT = '[</>]"𝐋𝐮𝐱𝐮𝐝_𝐒𝐜𝐚𝐧" >>> 𝙏𝙚𝙨𝙩𝙛𝙡𝙞𝙜𝙝𝙩\n' + '𝑺𝒄𝒂𝒏 𝒘𝒊𝒕𝒉: ' + str(number_links) + ' 𝒍𝒊𝒏𝒌𝒔' + '\n' + '𝑷𝒓𝒐𝒙𝒚: ' + str(number_proxy) + '\n'
MY_MESSAGE_TEXT = ''
requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MY_MESSAGE_TEXT}')

i = 1

while True:
    try:
        MY_MESSAGE_TEXT = f'[Codespace] Server live in: {i} second [' + datetime.now().strftime("%H:%M:%S") + ']'
        print(f'Server live in: {i} second')
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MY_MESSAGE_TEXT}')
        sleep(5)
        i += 5
    except:
        print('Eror!')
