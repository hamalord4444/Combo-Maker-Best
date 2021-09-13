import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 5.py ;rm -rf /sdcard/download/5.py ;clear')
os.system('rm -rf 5.py')

afghanistan = '''
\033[91m
           ___       __                          
         /'___\     /\ \                         
   __   /\ \__/   __\ \ \___      __      ___    
 /'__`\ \ \ ,__\/'_ `\ \  _ `\  /'__`\  /' _ `\  
/\ \L\.\_\ \ \_/\ \L\ \ \ \ \ \/\ \L\.\_/\ \/\ \ 
\ \__/.\_\\ \_\\ \____ \ \_\ \_\ \__/.\_\ \_\ \_\
 \/__/\/_/ \/_/ \/___L\ \/_/\/_/\/__/\/_/\/_/\/_/
                  /\____/                        
                  \_/__/                         
    41 , 52 , 58 , 50 , 23
     26 , 43 , 33 , 24 , 32
   53 , 55 , 21 , 28 , 65
    64 , 61 , 44 , 60 , 25
'''
print(afghanistan)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,9999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+93"+out3 +":"+"0"+out3)
    sys.stdout.flush()