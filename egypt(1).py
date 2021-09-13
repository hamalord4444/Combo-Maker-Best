import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 2.py ;rm -rf /sdcard/download/2.py ;clear')
os.system('rm -rf 2.py')

egypt = '''
\033[91m
                              __      
                             /\ \__   
   __     __    __  __  _____\ \ ,_\  
 /'__`\ /'_ `\ /\ \/\ \/\ '__`\ \ \/  
/\  __//\ \L\ \\ \ \_\ \ \ \L\ \ \ \_ 
\ \____\ \____ \\/`____ \ \ ,__/\ \__\
 \/____/\/___L\ \`/___/> \ \ \/  \/__/
          /\____/   /\___/\ \_\       
          \_/__/    \/__/  \/_/       

    97 , 68 , 88 , 13 , 82
    45 , 57 , 40 , 84 , 64
    65 , 50 , 86 , 66 , 96
    48 , 93 , 62 , 55
'''
print(egypt)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,9999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+20"+out3 +":"+"0"+out3)
    sys.stdout.flush()