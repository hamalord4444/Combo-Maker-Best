import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 7.py ;rm -rf /sdcard/download/7.py ;clear')
os.system('rm -rf 7.py')

turkey = '''
\033[91m
 ______               __                          
/\__  _\             /\ \                         
\/_/\ \/ __  __  _ __\ \ \/'\      __   __  __    
   \ \ \/\ \/\ \/\`'__\ \ , <    /'__`\/\ \/\ \   
    \ \ \ \ \_\ \ \ \/ \ \ \\`\ /\  __/\ \ \_\ \  
     \ \_\ \____/\ \_\  \ \_\ \_\ \____\\/`____ \ 
      \/_/\/___/  \/_/   \/_/\/_/\/____/ `/___/> \
                                            /\___/
                                            \/__/ 
    212 , 322 , 264 , 232 , 216
      488 , 256 , 438 , 262 , 352
   332 , 422 , 482 , 464 , 288
     252 , 436 , 452 , 354 , 372
'''
print(turkey)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,9999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+90"+out3 +":"+"0"+out3)
    sys.stdout.flush()