import os
import time
import shutil


files = os.listdir()


for file in files:
    try:
        orgname = file
        foldername = file[0:1]
        
        if not os.path.exists(foldername):
            os.mkdir(foldername)
        print(foldername + " is created")
        
        shutil.move(orgname,foldername)
        
    except FileExistsError:
        pass
