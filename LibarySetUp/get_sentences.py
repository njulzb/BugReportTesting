import pandas as pd

def get_sentences(file_path):
    original_file = file_path
    original_excel = pd.read_excel(original_file)
    bug_list = original_excel['主题']
    with open('buglist.txt','w+',encoding='utf-8') as targetFile:
        targetFile.writelines('\n'.join(bug_list))
    pd.DataFrame(bug_list).to_excel('buglist.xlsx',encoding='utf-8',index=False)

get_sentences('problems.xlsx')