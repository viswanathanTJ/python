import requests
import io
import re
import time
import clipboard
from bs4 import BeautifulSoup
url = 'https://agathiyarjanasidhar.blogspot.com/' 
start_time = time.time()
count = 0
while True:
    r = requests.get(url)
    file_like_obj = io.StringIO(r.text)
    lines = file_like_obj.read()
    soup = BeautifulSoup(lines,'html.parser')
    title = soup.findAll("h3", {"class": "post-title entry-title"})
    content = soup.findAll("div", {"class": "post-body entry-content"})
    length = len(soup.findAll("h3", {"class": "post-title entry-title"}))
    matchObj = re.findall(r'blog-pager-older-link\' href=\'(.*)\' id', lines) 
    url = matchObj[0]
    clipboard.copy(url)
    count += length
    print(str(count) + " Files created successfully")
    print("--- %s seconds ---" % (time.time() - start_time))
    for i in range(length):
        x = str(title[i])  
        clean = re.compile('<.*?>')
        x = re.sub(clean, '', x)       
        name = re.sub("[\/:*<?>|\"n.]", '', x[:200])      
        name = name.replace('\n','') 
        y = str(content[i])       
        y = re.sub(clean, '', y)
        file1 = open(name + ".txt","w",encoding='utf-8')
        file1.write(y[1:])