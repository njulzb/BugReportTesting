# _*_ coding:utf-8 _*_
import pandas as pd
import LibarySetUp.setupLib as lib

def test_all(test_case_file):
    test_case = pd.read_excel(test_case_file)
    result = {}
    count = 1
    # print(test_case['description'])
    for sentence in test_case['description']:
        result[sentence] = lib.calculate(sentence)
        print(count)
        count += 1
    pd.DataFrame.from_dict(result , orient='index').to_excel('result.xlsx',encoding='utf-8')

test_all('real_bug_sheet.xlsx')