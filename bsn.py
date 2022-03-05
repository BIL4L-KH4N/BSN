import os
os.system('termux-setup-storage')
os.system('git pull')
os.system('rm -rf file32.cpython-310.so')
os.system('rm -rf file.cpython-310.so')
from file32 import reg
reg()
