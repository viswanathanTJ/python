from flask import request, send_file, redirect
import pyautogui as p
import time
import os
import shutil
import subprocess
import clipboard


def scan():
    name = request.form['name']
    p.hotkey('win', '3')
    time.sleep(7)
    p.click(337,423)
    p.hotkey('ctrl', 'f2')
    time.sleep(2)
    p.press('enter')
    time.sleep(2)
    p.hotkey('alt', 'c')
    p.hotkey('alt', 'p')
    time.sleep(10)
    p.hotkey('alt', 's')
    time.sleep(25)
    fpath = 'L:/Horoscope/IMG.jpg'
    npath = 'L:/Horoscope/' + name + '.jpg'
    os.rename(fpath,npath)

def send():
    name = 'sendtophone'
    aname = request.form['aname']
    fname = request.form['fname']
    mname = request.form['mname']
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    hour = request.form['hours']
    min = request.form['minutes']
    ampm = request.form['time']
    gender = request.form['gender']
    place = request.form['place']
    check = request.form['check']
    try:
        os.remove("C:/KkcAstro/sendtophone.pdf")
    except FileNotFoundError:
        pass
    p.hotkey('win', '4')
    time.sleep(3)
    p.click(44, 39)
    p.click(60, 89)
    p.click(189, 87)
    time.sleep(1)
    if request.form['aname']:
        if check == "1":
            p.typewrite(aname)
            p.press('tab')
        else:
            clipboard.copy(aname)
            p.hotkey('ctrl', 'v')
            p.press('tab')
    else:
        p.press('tab')
    if request.form['fname']:
        if check == "1":
            p.typewrite(fname)
            p.press('tab')
        else:
            clipboard.copy(fname)
            p.hotkey('ctrl', 'v')
            p.press('tab')
    else:
        p.press('tab')
    if request.form['mname']:
        if check == "1":
            p.typewrite(mname)
            p.press('tab')
        else:
            clipboard.copy(mname)
            p.hotkey('ctrl', 'v')
            p.press('tab')
    else:
        p.press('tab')
    p.typewrite(date)
    p.press('right')
    p.typewrite(month)
    p.press('right')
    p.typewrite(year)
    p.hotkey('tab')
    p.typewrite(hour)
    p.press('right')
    p.typewrite(min)
    p.press('right')
    p.press('right')
    if ampm == 'am':
        p.typewrite('a')
    elif ampm == 'pm':
        p.typewrite('p')
    p.hotkey('tab')
    p.hotkey('tab')
    p.typewrite(place)
    if place == 'Salem':
        p.press('down')
    p.press('down')
    p.press('enter')
    if gender == 'female':
        p.click(912, 326)
    elif gender == 'male':
        p.click(836, 327)
    p.hotkey('alt', 'g')  # 1057,569
    time.sleep(2)
    p.click(321, 34)
    time.sleep(1)
    name = 'sendtophone'
    p.typewrite(name)
    p.press("enter")
    p.press("enter")
    time.sleep(1)
    p.click(1587, 13)
    p.click(393, 9)
    p.click(1116, 256)
    p.click(1569, 17)
    imgname = f'C:\\KkcAstro\\sendtophone.pdf'
    subprocess.Popen(imgname, shell=True)
    time.sleep(6)
    p.hotkey('enter')
    time.sleep(4)
    p.hotkey('f2')
    time.sleep(4)
    p.click(1587, 12)
    p.click(802, 340)
    os.remove("C:/KkcAstro/sendtophone.pdf")


def print():
    aname = request.form['aname']
    fname = request.form['fname']
    mname = request.form['mname']
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    hour = request.form['hours']
    min = request.form['minutes']
    ampm = request.form['time']
    gender = request.form['gender']
    place = request.form['place']
    check = request.form['check']
    p.hotkey('win', '4')
    time.sleep(4)
    p.click(44, 39)
    p.click(60, 89)
    p.click(189, 87)
    time.sleep(1)
    if request.form['aname']:
        if check == "1":
            p.typewrite(aname)
            p.press('tab')
        else:
            clipboard.copy(aname)
            p.hotkey('ctrl', 'v')
            p.press('tab')
    else:
        p.press('tab')
    if request.form['fname']:
        if check == "1":
            p.typewrite(fname)
            p.press('tab')
        else:
            clipboard.copy(fname)
            p.hotkey('ctrl', 'v')
            p.press('tab')
    else:
        p.press('tab')
    if request.form['mname']:
        if check == "1":
            p.typewrite(mname)
            p.press('tab')
        else:
            clipboard.copy(mname)
            p.hotkey('ctrl', 'v')
            p.press('tab')
    else:
        p.press('tab')
    p.typewrite(date)
    p.press('right')
    p.typewrite(month)
    p.press('right')
    p.typewrite(year)
    p.hotkey('tab')
    p.typewrite(hour)
    p.press('right')
    p.typewrite(min)
    p.press('right')
    p.press('right')
    if ampm == 'am':
        p.typewrite('a')
    elif ampm == 'pm':
        p.typewrite('p')
    p.hotkey('tab')
    p.hotkey('tab')
    p.typewrite(place)
    if place == 'Salem':
        p.press('down')
    p.press('down')
    p.press('enter')
    if gender == 'female':
        p.click(912, 326)
    elif gender == 'male':
        p.click(836, 327)
    p.hotkey('alt', 'g')
    time.sleep(2)
    p.click(221, 35)
    time.sleep(1)
    p.click(354, 411)
    p.click(1567, 9)
    p.click(1119, 262)
    p.click(1575, 12)
