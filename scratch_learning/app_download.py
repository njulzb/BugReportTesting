import requests
import time
from bs4 import BeautifulSoup
import re
import os
import threading

def download_app(projectName , version , rootPath):
    requests.adapters.DEFAULT_RETRIES = 1024
    s = requests.session()
    s.keep_alive = False
    head = 'https://github.com/'
    zipPath = '/archive/' + version + '.zip'
    issueOPenPath = '/labels/bug?q=is%3Aopen+label%3Abug'
    issueClosePath = '/issues?q=label%3Abug+is%3Aclosed'

    zipUrl = head + projectName + zipPath
    print(zipUrl)
    response = requests.get(zipUrl,False)
    with open( rootPath + '/' + version + '.zip','wb') as file:
        file.write(response.content)

    flag = True
    pageCount = 1
    while flag:
        issueOpenUrl = head + projectName + issueOPenPath + '&page=' + str(pageCount)
        pageCount += 1
        print(issueOpenUrl)
        response = requests.get(issueOpenUrl,False)
        openList = []
        openSoup = BeautifulSoup(response.text,'lxml')
        for item in openSoup.find_all('a','link-gray-dark v-align-middle no-underline h4 js-navigation-open',True):
            openList.append(item.get_text().strip())
        if len(openList)==0:
            flag = False
        mode = 'w+' if pageCount==2 else 'a+'
        with open(rootPath + '/open.txt',mode,encoding='utf-8') as file:
            file.write('\n'.join(openList))
        time.sleep(0.1)

    flag = True
    pageCount = 1
    while flag:
        issueCloseUrl = head + projectName +issueClosePath + '&page=' + str(pageCount)
        pageCount += 1
        print(issueCloseUrl)
        closeResponse = requests.get(issueCloseUrl,False)
        closeList = []
        closeSoup = BeautifulSoup(closeResponse.text, 'lxml')
        for item in closeSoup.find_all('a', 'link-gray-dark v-align-middle no-underline h4 js-navigation-open',True):
            closeList.append(item.get_text().strip())
        if len(closeList)==0:
            flag = False
        mode = 'w+' if pageCount == 2 else 'a+'
        with open(rootPath + '/close.txt',mode,encoding='utf-8') as file:
            file.write('\n'.join(closeList))
        time.sleep(0.1)


list = [['y20k/transistor',('v1.2.3','v1.1.5')],
        ['kriztan/Pix-Art-Messenger',('1.17.1','1.17.0')],
        ['helloworld1/AnyMemo',('10.10.1','10.9.992')],
        ['ankidroid/Anki-Android',('v2.8.1','v2.7beta1')],
        ['f-droid/fdroidclient',('v0.103.2','v0.98')],
        ['yeriomin/YalpStore',('0.17',)],
        ['Commit451/LabCoat',('2.2.4',)],
        ['codinguser/gnucash-android',('v2.1.4','v2.1.3','v2.0.5')],
        ['Ifsttar/NoiseCapture',('0.4.2b',)],
        ['connectbot/connectbot',('v1.9.2',)],
        ['scoute-dich/K9-MailClient',('v5.207.4',)],
        ['DCubix/OpenMF',('v1.0.1',)],
        ['erickok/transdroid',('v2.5.0-beta1',)],
        ['BoogieMAN2K/Beem',('v0.1.7rc1',)]]



for item in list:
    name = item[0]
    for version in item[1]:
        pathName = name.replace('/','-')
        if os.path.exists(pathName) is False:
            os.makedirs(pathName)
        # download_app(name,version,pathName)
        t = threading.Thread(target=download_app,args=(name,version,pathName))
        t.start()
        # time.sleep(100)

