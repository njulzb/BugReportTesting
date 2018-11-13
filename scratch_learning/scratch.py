import requests
from bs4 import BeautifulSoup
import re

def get_github_trend_by_frequence_and_language(frequence,language):
    resultList = []
    response = requests.get('https://github.com/trending' + language + frequence)
    soup = BeautifulSoup(response.text,'lxml')
    projects = soup.find_all('li', 'col-12 d-block width-full py-4 border-bottom')
    for eachProjects in projects:
        eachStars = eachProjects.find_all('a','muted-link d-inline-block mr-3')
        starsStr = (eachStars[0].get_text().strip())
        starsStr = starsStr.replace(',','')
        starsInt = int(starsStr)

        eachNameList = eachProjects.find_all('span','text-normal')
        eachName = (eachNameList[0].get_text().strip())
        resultList.append(eachName)

    return resultList

frequence = '?since=daily'
language = '/c++'
resultList = []
resultList = get_github_trend_by_frequence_and_language(frequence,language)
print(resultList)

