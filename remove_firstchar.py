import os
import time
import shutil


files = os.listdir()


for file in files:
    try:
        orgname = file
        foldername = file[1:]
        #print(foldername)
        os.rename(orgname,file[1:])
        # if not os.path.exists(foldername):
            # os.mkdir(foldername)
        # print(foldername + " is created")
        # shutil.move(orgname,foldername)
        # print("Files is moved to new folder "+ foldername)
    except FileExistsError:
        pass
