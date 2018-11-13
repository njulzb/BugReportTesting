# coding = utf-8
import jieba
import pandas as pd


def filter_sentences(sentence):
    sentence = sentence.replace('，','')
    sentence = sentence.replace('。','')
    sentence = sentence.replace('！','')
    sentence = sentence.replace('【','')
    sentence = sentence.replace('】','')
    sentence = sentence.replace('？','')
    sentence = sentence.replace(',','')
    sentence = sentence.replace('.','')
    sentence = sentence.replace('-','')
    sentence = sentence.replace('+','')
    sentence = sentence.replace('“','')
    sentence = sentence.replace('”','')
    sentence = sentence.replace('/','')
    return sentence



def cut_words(excel_file):
    sentences = pd.read_excel(excel_file,skiprows=1)
    result_array = []
    single_dict = {}
    double_dict = {}
    triple_dict = {}
    for index,line in sentences.iterrows():
        each_sentence = filter_sentences(line.values[0])
        word_generator = jieba.cut(each_sentence,cut_all=False)
        sentenceCutResult = []
        sentenceCutResult.append(each_sentence)
        pre1 = ''
        pre2 = ''
        for each_word in word_generator:
            single_dict[each_word] = single_dict.setdefault(each_word,0) + 1
            double_dict[(pre2 , each_word)] = double_dict.setdefault((pre2 , each_word),0) + 1
            triple_dict[(pre1 , pre2 , each_word)] = triple_dict.setdefault((pre1,pre2,each_word),0) + 1
            pre1 = pre2
            pre2 = each_word
            sentenceCutResult.append(each_word)

        result_array.append(sentenceCutResult)

    pd.DataFrame(result_array).to_excel('words_cut_result.xlsx',encoding='utf-8')
    pd.DataFrame(list(sorted(single_dict.items(),key=lambda x:x[1],reverse=True ))).to_excel('single_occurence.xlsx',encoding='utf-8',header=None,index=None,columns=None)
    pd.DataFrame(list(sorted(double_dict.items(),key=lambda x:x[1],reverse=True ))).to_excel('double_occurence.xlsx',encoding='utf-8',header=None,index=None,columns=None)
    pd.DataFrame(list(sorted(triple_dict.items(),key=lambda x:x[1],reverse=True ))).to_excel('triple_occurence.xlsx',encoding='utf-8',header=None,index=None,columns=None)



cut_words('buglist.xlsx')
