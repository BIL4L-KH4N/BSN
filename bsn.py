import os,platform
os.system('git pull')

bsn=platform.architecture()[0]
if bsn=="32bit":
    print('Sorry Update Your Phone...')
elif bsn=="64bit":
    __import__("bili")
