import requests
from bs4 import BeautifulSoup

def if_has_version(projectName , times):
    className = 'select-menu-item-text css-truncate-target'
    urlHead = 'https://github.com/'
    realUrl = urlHead + projectName
    res = requests.get(realUrl)
    soup = BeautifulSoup(res.text,'lxml')
    list = []
    for item in soup.find_all('span',className):
        list.append(item.get_text().strip())

    return True if len(list)>=5 else False


if_has_version('AntennaPod/AntennaPod',5)
