from glob import glob
import os
import re

files = glob('*.txt')

for f in files:
	a = open(f, 'r', encoding='utf-8').readline().strip()
	name = re.sub("[\/:, *<?>|\"n.]", '', a[:200])
	name = name.replace('\n', '')

	print('Renaming', name)

	os.rename(f, name+'.txt')
