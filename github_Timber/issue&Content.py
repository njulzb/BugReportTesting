# coding = utf-8
import requests
from bs4 import BeautifulSoup

# 这个方法是用来提取issue_content的
def getIssue_Content():

    # 这里是requests的设置
    requests.adapters.DEFAULT_RETRIES = 10
    s = requests.session()
    s.keep_alive = False

    # 这里是网站的链接地址，project 和url是可以修改的
    topURL = 'https://github.com/'
    projectURL = 'naman14/Timber'
    openURL = '/issues?q=is%3Aopen+is%3Aissue'
    closeURL = '/issues?q=is%3Aissue+is%3Aclosed'
    pageURL = '&page='

    realURL = topURL + projectURL + openURL + pageURL;
    # realURL = topURL + projectURL + closeURL + pageURL;
    page = 1
    while True:
        response = requests.get(realURL + str(page) , verify= False )
        page += 1
        soup = BeautifulSoup(response.text,'lxml')
        tagName = 'a'
        tagClass = 'link-gray-dark v-align-middle no-underline h4 js-navigation-open'
        flag = False
        for item in soup.find_all(tagName , tagClass , True):
            flag = True
            title = item.get_text().strip()
            href = item['href']
            splitList = href.split('/')
            num = splitList[len(splitList) - 1]
            moreResponse = requests.get(topURL + href,verify=False)
            moreSoup = BeautifulSoup(moreResponse.text,'lxml')
            commentsList = []
            for eachP in moreSoup.find_all('p'):
                commentsList.append(eachP.get_text().strip())

            # print(commentsList)
            # print(commentsList[4:])
            with open('open/'+str(num) + '.txt' , 'w+' , encoding='utf-8') as file:
                file.write('title:' + title + '\n\n')
                file.writelines('\n'.join(commentsList[4:]))

        if flag is False:
            break


getIssue_Content()