import requests
from bs4 import BeautifulSoup



def get_issue_from_github(projectName, type):
    requests.adapters.DEFAULT_RETRIES = 3
    s = requests.session()
    s.keep_alive = False

    githubHead = 'https://github.com/'
    prefix = '/labels/bug?q=is%3Aopen+label%3Abug' if type=='open' else '/issues?q=label%3Abug+is%3Aclosed'
    realURL = githubHead + projectName + prefix

    pageCount = 1
    resultList = []
    while True:
        pageParam = '&page=' + str(pageCount)
        pageCount += 1
        try:
            response = requests.get(realURL + pageParam , verify = False , timeout = 100)
        except BaseException:
            continue
        print('respone from :' , response.url)

        soup = BeautifulSoup(response.text , 'lxml')
        tempList = []
        tagName = 'a'
        tagClass = 'link-gray-dark v-align-middle no-underline h4 js-navigation-open'
        for item in soup.find_all(tagName , tagClass , True):
            tempList.append(item.get_text().strip())
        if len(tempList) == 0:
            break
        resultList.extend(tempList)
        response.close()
    return resultList



# 示例操作
# open bug issue
# print(get_issue_from_github('AntennaPod/AntennaPod', 'open'))
# close bug issue
# print(get_issue_from_github('AntennaPod/AntennaPod', 'close'))

projectNameList = []
with open('searchList1.txt' , 'r+') as file:
    projectNameList = file.readlines()

for item in projectNameList:
    openList = get_issue_from_github(item,'open')
    closeList = get_issue_from_github(item,'close')
    with open(item + 'open.txt' , 'w+') as file:
        file.write('\n'.join(openList))
    with open(item + 'close.txt' , 'w+') as file:
        file.write('\n'.join(closeList))
