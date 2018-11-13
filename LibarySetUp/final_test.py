# _*_ coding:utf-8 _*_
import pandas as pd
import LibarySetUp.setupLib as lib

def test_all(test_case_file):
    test_case = pd.read_excel(test_case_file)
    result = {}
    count = 1
    for sentence in test_case['主题']:
        result[sentence] = lib.calculate(sentence)
        print(count)
        count += 1
    pd.DataFrame(result).to_excel('result.xlsx',encoding='utf-8')

test_all('buglist.xlsx')