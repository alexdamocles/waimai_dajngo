import requests
import re
def get1():
    url1="http://127.0.0.1:1111"
    html = requests.get(url1)
    #html.encoding = 'gbk'
    h1=html.text
    print(h1)

print(get1())