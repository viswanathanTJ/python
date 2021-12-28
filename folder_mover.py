import os
import glob
import shutil

fdir = r'B:\Notepad\Notepad'
os.chdir(fdir)
files = glob.glob('*.txt')
varisai = ' வரிசை'

global success_count
success_count = 0

def move(fname):
    global success_count
    fsrc = fdir + '\\' + fname
    print('fsrc', fsrc)
    fdest = os.getcwd()
    print('fdest', fdest)
    try:
        # shutil.move(fsrc,fdest) # Don't overwrite
        shutil.move(fsrc, os.path.join(fdest, fname))
        print('Completed:', fname)
        success_count = success_count + 1
    except:
        print('Error on Moving:', fname)

def e(arg):
    return os.path.exists(arg)

for file in files:
    os.chdir(fdir)
    print('Processing:', file)
    try:
        fc = file[0]
        sc = file[1]
        tc = file[2]
        foc = file[3]
        fic = file[4]
        sic = file[5]

        if e('ஸ்ரீ வரிசை'):
            os.chdir('ஸ்ரீ வரிசை')
            print('done')
            if e('ஸ்ரீ'+fic):
                os.chdir('ஸ்ரீ'+fic)
                move(file)
            else:
                os.chdir(fdir)
        
        if e(fc):
            shutil.move(os.path.join(fdir, file), os.path.join(os.path.join(fdir, fc), file))
            # shutil.move(file, fc) # dont overwrite
        elif e(fc+varisai):
            os.chdir(fc+varisai)
            if e(fc+sc+varisai):
                os.chdir(fc+sc+varisai) 
                if e(fc+sc+tc+varisai): 
                    os.chdir(fc+sc+tc+varisai)
                    move(file)
                elif e(fc+sc+tc):
                    os.chdir(fc+sc+tc)
                    move(file)
                elif e(fc+sc+tc+foc+fic):
                    os.chdir(fc+sc+tc+foc+fic)
                    move(file)
                elif e(fc+sc+tc+foc+fic+varisai):
                    os.chdir(fc+sc+tc+foc+fic+varisai)
                    if e(fc+sc+tc+foc+fic+sic):
                        os.chdir(fc+sc+tc+foc+fic+sic)
                        move(file)
            elif e(fc+sc+tc):
                os.chdir(fc+sc+tc)
                move(file)
            elif e(fc+sc):
                os.chdir(fc+sc)
                move(file)
            elif e(fc):
                os.chdir(fc)
                move(file)
            elif e(fc+varisai):
                os.chdir(fc+varisai)
                if e(fc+sc):
                    os.chdir(fc+sc)
                    move(file)
                elif e(fc+sc+varisai):
                    os.chdir(fc+sc+varisai)
                    if e(fc+sc+tc):
                        os.chdir(fc+sc+tc)
                        move(file)
                    elif e(fc+sc+tc+varisai):
                        os.chdir(fc+sc+tc+varisai)
                        if e(fc+sc+tc+foc+fic+sic):
                            os.chdir(fc+sc+tc+foc+fic+sic)
                            move(file)
                        elif e(fc+sc+tc+foc):
                            os.chdir(fc+sc+tc+foc)
                            move(file)
                    elif e(fc+sc+tc+foc):
                        os.chdir(fc+sc+tc+foc)
                        move(file)           
    except Exception as er:
        print('Some Error while Processing:', file)
        print(er)

print('Total File:', len(files))
print('Success:', success_count)
