import requests
from bs4 import BeautifulSoup

def scratch_from_gitlab():
    url = 'https://gitlab.com/fdroid/fdroidclient/issues?scope=all'
    stateStr = '&state='
    pageStr = '&page='

    # scratch open
    flag = True
    openList = []
    pageCount = 1
    while flag:
        stateParam = 'opened'
        realUrl = url + stateStr + stateParam + pageStr + str(pageCount)
        response = requests.get(realUrl)
        responseUrl = response.url
        if responseUrl != realUrl:
            flag = False
        print(url + stateStr + stateParam + pageStr + str(pageCount))
        pageCount += 1
        openSoup = BeautifulSoup(response.text,'lxml')


        for item in openSoup.find_all('span','issue-title-text'):
            text = item.find_all('a')[0].get_text()
            openList.append(text)

    with open('openIssue.txt' , 'w+' , encoding='utf-8') as file:
        file.write('\n'.join(openList))

    print(len(openList))

    # scratch close
    flag = True
    closeList = []
    pageCount = 1
    while flag:
        stateParam = 'closed'
        realUrl = url + stateStr + stateParam + pageStr + str(pageCount)
        response = requests.get(realUrl)
        responseUrl = response.url
        if responseUrl != realUrl:
            flag = False
        print(realUrl)
        pageCount += 1
        openSoup = BeautifulSoup(response.text, 'lxml')

        for item in openSoup.find_all('span', 'issue-title-text'):
            text = item.find_all('a')[0].get_text()
            closeList.append(text)

    with open('closeIssue.txt', 'w+',encoding='utf-8') as file:
        file.write('\n'.join(closeList))

    print(len(closeList))


scratch_from_gitlab()