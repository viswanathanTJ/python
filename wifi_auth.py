from os import system
from requests import Session, post, request
import urllib3

username = '21mcr119'
password = 'viswa@21'
print('Signing in')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url_1 = 'http://www.google.co.in'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
session = Session()
res = session.get(url_1, headers=headers)
magic = res.url.split('?')[1]
payload = {
    '4Tredir': 'http://google.com/',
    'magic': str(magic),
    'username': username,
    'password': password,
}
r = request("GET", 'https://www.gstatic.com/generate_204', verify=False)
url_2 = r.url
res = post(url_2, headers=headers, data=payload, verify=False)
system(f"start {res.url}")
print('Successfully authenticated, now closing.. Bye.. :)')
