import subprocess
from time import sleep
import pyautogui as p
import os



if name == '':
    quit()
    
# Start Scan Photoshop
os.startfile(
    "C:\Program Files\Adobe\Adobe Photoshop CS4 (64 Bit)\Photoshop.exe")
sleep(4)
p.click(1137, 423)
p.press('f2')
sleep(1)
p.press('enter')
p.hotkey('alt', 'c')
p.hotkey('alt', 's')
p.hotkey('alt', 'tab')



name = input('Enter name: ')
fpath = f'I:\\Customers\\Horoscope\\{name}.jpg'

while os.path.isfile(fpath):
    print('File name already Exists')
    name = input('Enter new name:')
    fpath = f'I:\\Customers\\Horoscope\\{name}.jpg'

p.hotkey('alt', 'tab')

# sleep(15)
sleep(1)
p.hotkey('ctrl', 'shift', 's')
sleep(1)
p.typewrite(name)
sleep(1)
p.press('enter')
sleep(1)
p.press('enter')
p.hotkey('alt','f4')

fpath = f'I:\\Customers\\Horoscope\\BalaPrasanth.jpg'
name = 'Dad'
subprocess.run([r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe', 'web.whatsapp.com'])
sleep(5)
p.click(480, 168) # input name
sleep(.1)
p.typewrite(name)
sleep(.5)
p.click(402,287) # user select
sleep(.5)
p.click(754, 975) # pin icon
sleep(.2)
p.click(750, 911) # camera icon
sleep(.5)
p.typewrite(fpath) # url paster
sleep(.5)
p.press('enter')
sleep(.5)
p.press('enter') # confirm send
sleep(2)
p.click(754, 975) # pin icon
sleep(.2)
p.click(754, 708) # doc icon
sleep(.5)
p.typewrite(fpath) # url paster
p.press('enter')
sleep(.3)
p.press('enter') # confirm send

p.hotkey('alt','f4')
