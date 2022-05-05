import eyed3
import os
import re
os.chdir('E:\Music\Daily Mix 3')
dir = os.listdir()
audios = [x for x in dir if x[-4:]=='.mp3']
for file in audios:
    audiofile = eyed3.load(file)
    name = re.sub("[\/:,*<?>|\"n.]", '', audiofile.tag.title[:200]).replace('\n', '')
    print(audiofile.tag.title, '->', name)
    try:
        os.rename(file, name+'.mp3')
    except FileExistsError:
        if not os.path.exists('dups\\'+name+'.mp3'):
            os.rename(file, 'dups\\'+name+'.mp3')
