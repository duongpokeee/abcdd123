import random
from time import sleep
import os

try:
	try:
		os.system('pip install random')
	except:
		os.system('pip3 install random')
except:
	print('Eror!')

i = 0

while True:
	print(f'{i} ~~> ' + random.choice(["apple", "banana", "cherry", "orange", "grape", "mango", "pineapple", "strawberry", "blueberry", "watermelon","car", "motorbike", "bicycle", "train", "airplane", "boat", "submarine", "helicopter", "rocket","dog", "cat", "elephant", "tiger", "lion", "giraffe", "monkey", "rabbit", "panda", "dolphin","table", "chair", "sofa", "bed", "lamp", "television", "laptop", "phone", "watch", "camera","pen", "book", "notebook", "eraser", "ruler", "calculator", "backpack", "scissors", "glue", "marker"]) + random.choice(['1','2','3','4','5','6','7','8','9','0']) + random.choice(['code','dev','py','node','html','hello','source','note','php','golang']) + random.choice(['!','@','#','$','%','&']))
	i += 1
	sleep(1)
