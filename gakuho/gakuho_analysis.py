import MeCab
import re
import matplotlib.pyplot as plt
import MeCab
import re
import matplotlib.pyplot as plt
import collections

def format_text(text):
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(r'[!-~]', "", text)#半角記号,数字,英字
    text=re.sub(r'[︰-＠]', "", text)#全角記号
    text=re.sub('\n', " ", text)#改行文字
    text=re.sub('…', " ", text)
    text=re.sub('、', " ", text)
    text=re.sub('。', " ", text)
    text=re.sub(" ","",text)

    return text

m = MeCab.Tagger('-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

with open("united.txt",encoding="UTF-8") as f:
    text = f.read()
text = format_text(text)

#str型で、単語が空白で別れる
str_output = m.parse(text)

#listに変換する
list_output = str_output.split(' ')
list_output2 = []

re_hiragana = re.compile(r'^[あ-ん]+$')

for i in list_output:
    if len(i)!=1:
        if not re_hiragana.fullmatch(i):
            list_output2.append(i)
        
list_output3 = collections.Counter(list_output2)
learning_data = " ".join(list_output2)
with open("data.txt",mode="w",encoding="UTF-8") as f:
    f.write(learning_data)

from gensim.models import word2vec
data = word2vec.Text8Corpus("data.txt")
model = word2vec.Word2Vec(data, size=200)

while True:
    print("検索ワード")
    try: 
        ret = model.wv.most_similar(positive=input(">> "))
        for item in ret:
                print(item[0], item[1])
    except:
        print("No hit")