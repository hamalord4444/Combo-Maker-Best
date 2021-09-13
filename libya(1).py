import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 6.py ;rm -rf /sdcard/download/6.py ;clear')
os.system('rm -rf 6.py')

libya = '''
\033[91m
 __       __                          
/\ \     /\ \                         
\ \ \    \ \ \____  __  __     __     
 \ \ \  __\ \ '__`\/\ \/\ \  /'__`\   
  \ \ \L\ \\ \ \L\ \ \ \_\ \/\ \L\.\_ 
   \ \____/ \ \_,__/\/`____ \ \__/.\_\
    \/___/   \/___/  `/___/> \/__/\/_/
                        /\___/        
                        \/__/         
    21 , 22 , 23 , 24 , 25
     26 , 31 , 41 , 51 , 54
   57 , 61 , 63 , 64 , 67
    71 , 81 , 87
'''
print(libya)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,9999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+218"+out3 +":"+"0"+out3)
    sys.stdout.flush()