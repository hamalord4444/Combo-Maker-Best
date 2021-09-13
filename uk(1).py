import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 8.py ;rm -rf /sdcard/download/8.py ;clear')
os.system('rm -rf 8.py')

UK = '''
\033[91m
 __  __  __  __     
/\ \/\ \/\ \/\ \    
\ \ \ \ \ \ \/'/'   
 \ \ \ \ \ \ , <    
  \ \ \_\ \ \ \\`\  
   \ \_____\ \_\ \_\
    \/_____/\/_/\/_/
                    
                    
    20 , 23 , 24 , 28 , 29
'''
print(UK)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,99999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+44"+out3 +":"+"0"+out3)
    sys.stdout.flush()
