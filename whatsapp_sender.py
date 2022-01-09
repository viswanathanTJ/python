import sys
import os
from dateutil import parser
import glob
import pyautogui as p
import subprocess
from time import sleep

try:
    name = sys.argv[1]
except:
    print('No args passed\nSending last file')
    name = '1'

def sender(file):
    p.click(759, 1032) # pin icon
    sleep(.2)
    p.click(751, 963) # camera icon
    sleep(.2)
    p.typewrite(file) # url paster
    sleep(.2)
    p.press('enter')
    sleep(1)
    p.press('enter') # confirm send
    sleep(2)
    p.click(759, 1032) # pin icon
    sleep(.2)
    p.click(753, 770) # doc icon
    sleep(.2)
    p.typewrite(file) # url paster
    p.press('enter')
    sleep(1)
    p.press('enter') # confirm send


def main():
    if name.isdigit():
        counts = int(name)
        files = glob.glob('/mnt/PHOTOS/1Customers/Horoscopes/*.jpg')
        files.sort(key=os.path.getmtime, reverse=True)
        current_index = 0
        while counts > 0:
            current_file = files[current_index]
            if 'IMG.jpg' in current_file:
                current_index += 1
                continue
            sender(current_file)
            print(current_file)
            current_index += 1
            counts -= 1
            sleep(1)
    else:
        sender('/mnt/PHOTOS/1Customers/Horoscopes/'+name+'.jpg')

def open():
    sleep(5)
    p.click(451, 205) # input name
    sleep(.1)
    p.typewrite('Dad')
    sleep(.5)
    p.click(431,335) # user select
    sleep(.5)

if __name__ == '__main__':
    subprocess.run(['/usr/bin/brave', '--user-data-dir-name="/home/siva/.config/BraveSoftware/Brave-Browser/Profile 1"', 'web.whatsapp.com'])
    open()
    main()
