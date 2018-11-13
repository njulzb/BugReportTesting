# coding = utf-8
import pandas as pd
import jieba
import LibarySetUp.word_segment as seg



def setupLib(single_excel , double_excel , triple_excele):
    origin_single_dict = pd.read_excel(single_excel,header=None).set_index(0).T.to_dict('list')
    origin_double_dict = pd.read_excel(double_excel,header=None).set_index(0).T.to_dict('list')
    origin_triple_dict = pd.read_excel(triple_excele,header=None).set_index(0).T.to_dict('list')

    single_dict = {}
    double_dict = {}
    triple_dict = {}
    for key,value in origin_single_dict.items():
        single_dict[key] = value[0]
    for (key,value) in origin_double_dict.items():
        double_dict[tuple(eval(key))] = value[0]
    for key,value in origin_triple_dict.items():
        triple_dict[tuple(eval(key))] = value[0]

    return (single_dict , double_dict , triple_dict)


def calculate(sentence):
    (single_dict , double_dict , triple_dict) = setupLib('single_occurence.xlsx','double_occurence.xlsx','triple_occurence.xlsx')
    sentence = seg.filter_sentences(sentence)
    words_generator = jieba.cut(sentence,cut_all=False)

    bi_gram = 1
    tri_gram = 1
    pre1 = ''
    pre2 = ''
    for each_word in words_generator:
        #这里对没有出现过的语料应该怎么做
        bi_gram *= double_dict.setdefault((pre2,each_word),1e-20) / (1+single_dict.setdefault(pre2,0))
        tri_gram *= triple_dict.setdefault((pre1,pre2,each_word),1e-20) / (1+double_dict.setdefault((pre1,pre2),0))
        pre1 = pre2
        pre2 = each_word
    return (bi_gram , tri_gram)



# (bi_gram , tri_gram) = calculate('【V1.0.0+Test1】【PC申请】我的办件界面查询条件区域，时间条件不能选择需要手动输入',single_dict,double_dict,triple_dict)
# print(bi_gram,tri_gram)