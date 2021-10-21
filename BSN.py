import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')
    os.system('git pull')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from BSN import approval
    approval()
elif bit == '32bit':
    from BSN BSN approval
    approval()
