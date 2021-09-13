import os
import sys
import random
import time
import datetime
from random import *
os.system('rm -rf /sdcard/combo.txt')
os.system('rm -rf 1.py ;rm -rf /sdcard/download/1.py ;clear')
os.system('rm -rf 1.py')

iraq = '''\033[91m
\033[91m
                               
 __                            
/\_\  _ __    __       __      
\/\ \/\`'__\/'__`\   /'__`\    
 \ \ \ \ \//\ \L\.\_/\ \L\ \   
  \ \_\ \_\\ \__/.\_\ \___, \  
   \/_/\/_/ \/__/\/_/\/___/\ \ 
                          \ \_\
                           \/_/

     770 , 771 , 772 , 773 , 774
      750 , 751 , 752 , 753 , 754
     780 , 781 , 782 , 783 , 784
'''
print(iraq)
num = input('\033[94m CHOOSE CODE <> ')

for o in range (1000000):
    out = str(randint(0,9999999))
    sys.stdout=open("/sdcard/combo.txt", "a")
    out3 =num+out
    print("+964"+out3 +":"+"0"+out3)
    sys.stdout.flush()