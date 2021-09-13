import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 3.py ;rm -rf /sdcard/download/3.py ;clear')
os.system('rm -rf 3.py')

saudi = '''
\033[91m
                            __         
                           /\ \  __    
  ____     __     __  __   \_\ \/\_\   
 /',__\  /'__`\  /\ \/\ \  /'_` \/\ \  
/\__, `\/\ \L\.\_\ \ \_\ \/\ \L\ \ \ \ 
\/\____/\ \__/.\_\\ \____/\ \___,_\ \_\
 \/___/  \/__/\/_/ \/___/  \/__,_ /\/_/
                                       
                                       

    977 , 11 , 12 , 13 , 14
     16 , 17 , 50 , 53 , 55
    51 , 54 , 56 , 58 , 59
'''
print(saudi)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,9999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+966"+out3 +":"+"0"+out3)
    sys.stdout.flush()