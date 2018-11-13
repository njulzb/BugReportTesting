import requests
import time
from bs4 import BeautifulSoup

def search_project(search_key):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False

    githubHead = 'https://github.com/search?type=Repositories&q='
    realURL = githubHead + search_key

    pageCount = 1
    resultList = []

    while True:
        pageParam = '&p=' + str(pageCount)
        pageCount += 1
        try:
            response = requests.get(realURL + pageParam  ,verify = False , timeout = 100)
            time.sleep(10)
        except BaseException:
            continue
        # response = requests.get(realURL + pageParam, verify=False, timeout=1)
        print('response from ' , response.url)

        soup = BeautifulSoup(response.text , 'lxml')
        tempList = []
        # print(soup)
        # print(soup.find_all('a' , 'v-align-middle'))
        for item in soup.find_all('a' , 'v-align-middle'):
            tempList.append(item['href'])

        print(tempList)
        # if len(tempList) == 0 :
        #     break
        if pageCount >= 100:
            break
        # with open('searchlist.txt','a+') as f:
        #     f.write('\n'.join(tempList))
        resultList.extend(tempList)

    response.close()
    return resultList


with open('searchList1.txt','w+') as file:
    file.write('\n'.join(search_project('android')))
# print(search_project('android'))
