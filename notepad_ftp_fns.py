from ftplib import FTP
from datetime import date
import time
import glob
import shutil
import os


HOST = "192.168.0.3"
PORT = 2121


def download_notepad_files():

    shutil.copytree(r'skeleton', fdir)

    filenames = ftp.nlst('Notepad/0')

    print('Downloading files in folder 0...')
    for filename in filenames:
        with open('Notepad/0/' + filename, "wb") as file:
            ftp.retrbinary("RETR Notepad/0/"+filename, file.write)

def move(fname, dest):
    fsrc = fdir + '/' + fname
    fdest = os.getcwd() + '/' + dest
    try:
        # shutil.move(fsrc,fdest) # Don't overwrite        
        shutil.move(fsrc,os.path.join(fdest, fname))
    except:
        pass


def move_files():

    for f in glob.glob("Notepad/0/*.txt"):
        shutil.move(f, 'Notepad')

    varisai = ' வரிசை'
    os.chdir(fdir)
    files = glob.glob('*.txt')
    for file in files:
        os.chdir(fdir)
        try:
            fc = file[0]
            sc = file[1]
            tc = file[2]
            if os.path.exists(fc):
                shutil.move(file,fc)
            elif os.path.exists(fc+varisai):
                os.chdir(fc+varisai)
                if os.path.exists(fc+sc+varisai):
                    os.chdir(fc+sc+varisai)
                    if os.path.exists(fc+sc+tc):
                        move(file,fc+sc+tc)
                elif os.path.exists(fc+sc):              
                    move(file,fc+sc)
                elif os.path.exists(fc):
                    move(file,fc)
                elif os.path.exists(fc+varisai):
                    os.chdir(fc+varisai) 
                    if os.path.exists(fc+sc):
                        move(file,fc+sc)          
        except:
            print('Some Error while Moving:', file)

    os.chdir(fdir)

    files = glob.glob('*.txt')

    if files:
        remove_first_char(files)

def remove_first_char(files):
    os.chdir(fdir)
    for file in files:
        try:
            os.rename(file,file[1:])
        except FileExistsError:
            print('Error:', file)
    move_files()


def send_files(path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            ftp.storbinary('STOR ' + name, open(localpath,'rb'))
        elif os.path.isdir(localpath):
            # ftp.mkd(name)
            ftp.cwd(name)
            send_files(localpath)
            ftp.cwd("..")


def end_all():
    print('Deleting existing files in folder 0')
    filenames = ftp.nlst('0')
    for filename in filenames:
        ftp.delete('0/' + filename)
    print('Renaming and quitting...')
    todays_date = date.today()
    os.chdir(mdir)
    os.rename('Notepad', 'Notepad_'+str(todays_date))
    ftp.quit()

if __name__ == '__main__':
    o_start = time.time()
    mdir = os.getcwd()
    fdir = mdir + '\\Notepad'
    ftp = FTP()
    ftp.encoding='utf-8'
    ftp.connect(HOST, PORT)
    ftp.login('anonymous','anonymous')
    download_notepad_files()
    print('Moving files to respective folders...')
    move_files()
    print('Sending files to device...')
    ftp.cwd('Notepad')
    send_files(fdir)
    end_all()
    print('*** Script end successfully ***')
    print(f"Total time taken is {time.time() - o_start}")