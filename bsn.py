import os,platform
os.system('git pull')

bsn=platform.architecture()[0]
if bsn=="32bit":
    __import__("bn").reg()
elif bsn=="64bit":
    __import__("bs").reg()
