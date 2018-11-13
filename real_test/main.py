from real_test import word_segment,get_sentences

def set_up_lib_main(srcfile):
    get_sentences.get_sentences(srcfile , 'buglist.xlsx')
    word_segment.cut_words('buglist.xlsx')



set_up_lib_main('problems.xlsx')