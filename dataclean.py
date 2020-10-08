#coding:utf-8
'''
输入一段字符串即可
'''
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
def clear_text(line,clear_stop = True):
    ret_list = False
    if isinstance(line,list):
        line = " ".join(line)
        ret_list = True
    line = line.lower()
    p1 = re.compile(r'-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-')
    p2 = re.compile(r'[(][: @ . , ？！\s][)]')
    p3 = re.compile(r'[「『\\\\]')
    p4 = re.compile(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）0-9 , : ; \-\ \[\ \]\ \\]')
    line = p1.sub(r' ', line)
    line = p2.sub(r' ', line)
    line = p3.sub(r' ', line)
    line = p4.sub(r' ', line)
    line = " ".join(line.split())
    if clear_stop:
        from nltk.corpus import stopwords
        english_stopwords = stopwords.words('english')
        line = " ".join([word for word in line.split() if not word in english_stopwords])
 
    porter2 = nltk.stem.WordNetLemmatizer()
    line = [porter2.lemmatize(x) for x in nltk.word_tokenize(line)]
    line = [i for i in line if len(i)>2]
    if not ret_list:
        return " ".join(line)
    return line


