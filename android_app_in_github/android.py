import requests
import time
from bs4 import BeautifulSoup
import os
import threading

def if_has_issue(projectName):
    print('test issue')
    className ="js-selected-navigation-item selected reponav-item"
    urlHead = 'https://github.com/'
    realUrl = urlHead + projectName
    try:
        res = requests.get(realUrl,verify = False , timeout = 10)
        print('issue url = ',res.url)
    except BaseException:
        return False
    soup = BeautifulSoup(res.text,'lxml')
    s = soup.find_all("span","Counter")
    if len(s)<=0:
        return
    print('issue number = ',s[0].get_text())

    return True if int(s[0].get_text()) >= 50 else False


def if_has_version(projectName , times):
    print('test version')
    className = 'select-menu-item-text css-truncate-target'
    urlHead = 'https://github.com/'
    realUrl = urlHead + projectName
    print(realUrl)
    try:
        res = requests.get(realUrl,verify = False , timeout = 10)
        print('version url = ',res.url)
    except BaseException:
        return
    soup = BeautifulSoup(res.text,'lxml')
    list = []
    for item in soup.find_all('span',className):
        list.append(item.get_text().strip())

    res.close()
    print('version number = ' , len(list))
    return True if len(list)>=5 else False



def download_app(projectName , rootPath):
    head = 'https://github.com/'

    issueOPenPath = '/labels/bug?q=is%3Aopen+label%3Abug'
    issueClosePath = '/issues?q=label%3Abug+is%3Aclosed'


    flag = True
    pageCount = 1
    while flag:
        issueOpenUrl = head + projectName + issueOPenPath + '&page=' + str(pageCount)
        pageCount += 1
        try:
            response = requests.get(issueOpenUrl,verify = False , timeout = 10)
            print(response.url)
        except BaseException:
            return False
        openList = []
        openSoup = BeautifulSoup(response.text,'lxml')
        for item in openSoup.find_all('a','link-gray-dark v-align-middle no-underline h4 js-navigation-open',True):
            openList.append(item.get_text().strip())
        if len(openList)==0:
            flag = False
        mode = 'w+' if pageCount==2 else 'a+'
        with open(rootPath + '/open.txt',mode,encoding='utf-8') as file:
            file.write('\n'.join(openList))
        # time.sleep(0.1)

    flag = True
    pageCount = 1
    while flag:
        issueCloseUrl = head + projectName +issueClosePath + '&page=' + str(pageCount)
        pageCount += 1
        try:
            closeResponse = requests.get(issueCloseUrl,verify = False , timeout = 10)
            print(closeResponse.url)
        except BaseException:
            return False

        closeList = []
        closeSoup = BeautifulSoup(closeResponse.text, 'lxml')
        for item in closeSoup.find_all('a', 'link-gray-dark v-align-middle no-underline h4 js-navigation-open',True):
            closeList.append(item.get_text().strip())
        if len(closeList)==0:
            flag = False
        mode = 'w+' if pageCount == 2 else 'a+'
        with open(rootPath + '/close.txt',mode,encoding='utf-8') as file:
            file.write('\n'.join(closeList))
        # time.sleep(0.1)

    response.close()
    # if len(openList) + len(closeList) > 100:
    #     return True



list = ['AntennaPod/AntennaPod',
        'pockethub/PocketHub',
        'zxing/zxing',
        'BoD/android-contentprovider-generator',
        'bumptech/glide',
        'ManuelPeinado/MultiChoiceAdapter',
        'Tapadoo/Alerter',
        'k0shk0sh/FastHub',
        ]



list = []
print('before open name list')
with open('searchList1.txt','r+') as file:
    for line in file.readlines():
        list.append(line.strip())


requests.adapters.DEFAULT_RETRIES = 2
s = requests.session()
s.keep_alive = False

projectNameList = []
print('begin iteration')
count = 0
for item in list:
    print('count=',count)
    count += 1
    if not if_has_issue(item):
        print('issue not satisfied')
        continue

    if not if_has_version(item,5):
        print('version not satisfied')
        continue

    print('satisfied')
    name = item
    pathName = name.replace('/','-')
    if os.path.exists(pathName) is False:
        os.makedirs(pathName)
    download_app(name,pathName)
    # if flag :
    projectNameList.append('https://github.com/' + item)
    print('length of project name list',len(projectNameList))
    # t = threading.Thread(target=download_app,args=(name,pathName))
    # t.start()
    # time.sleep(100)

with open('projectNameList.txt','w+') as file:
    file.write('\n'.join(projectNameList))

