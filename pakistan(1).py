import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 4.py ;rm -rf /sdcard/download/4.py ;clear')
os.system('rm -rf 4.py')

pakistan = '''
\033[91m
 ____          __         
/\  _`\       /\ \        
\ \ \L\ \ __  \ \ \/'\    
 \ \ ,__/'__`\ \ \ , <    
  \ \ \/\ \L\.\_\ \ \\`\  
   \ \_\ \__/.\_\\ \_\ \_\
    \/_/\/__/\/_/ \/_/\/_/
                          
                          
    21 , 42 , 31 , 51 , 22
     47 , 65 , 74 , 61 , 66
   44 , 91 , 81 , 68 , 40
    48 , 56 , 52 , 71 , 46
'''
print(pakistan)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,9999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+92"+out3 +":"+"0"+out3)
    sys.stdout.flush()