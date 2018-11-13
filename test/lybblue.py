# coding = utf-8
import requests
from bs4 import BeautifulSoup
import os
import time

requests.adapters.DEFAULT_RETRIES = 3#这里设置重连次数
s = requests.session()
s.keep_alive = False

URL = 'https://s3.amazonaws.com/com.dataturks.imagemoderation/nudenumber.jpg'
if os.path.exists('happy_tonight') is False:
    os.makedirs('happy_tonight')
for i in range(1,70):
    count = '%02d' % i
    realURL = URL.replace('number' , count)
    response = requests.get(realURL ,verify=False, timeout = 200)#这里设置多久算失败
    print(count , response.url)
    with open('happy_tonight/' + count + '.jpg' , 'wb+') as pic:
        pic.write(response.content)
    time.sleep(1)#这里停一下
