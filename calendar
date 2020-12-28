import wget
import os
from threading import Thread

os.chdir("../calendar/2021/1")

def get_cal(date):
    url = "https://srirangaminfo.com/cal/2021/big/%02d01.jpg" % date
    image_filename = wget.download(url)
    print(f'\n{image_filename} Downloaded')

for i in range(1,32):
    t1 = Thread(target=get_cal, args=(i,))
    t1.start()
