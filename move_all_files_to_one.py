import os

source = r'M:\Workspace\Notepad\fastnote' + '\\'
errors = r'M:\\Workspace\Notepad\\errors' + '\\'

for (root, dirs, files) in os.walk(source):
    if files:
        for file in files:
            try:
                if not os.path.isfile(source+file):
                    os.rename(root+'\\'+file, source+file)
                else:
                    os.rename(root+'\\'+file, errors+file)
            except:
                print(root+'\\'+file)