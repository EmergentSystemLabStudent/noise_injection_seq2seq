# coding=utf-8

"""
LSTMの別で学習できるように作成するために作成するスクリプト作成する
出力形式

"""

import matplotlib.pylab as plt
import  numpy as np
import datetime
import pickle
import os
import glob
import sys
import math
import MeCab
import pandas as pd

#評価方法を調べる

#kerasｎついてModel(a,b)でaを入力としてbを出力するためにのそうを含まれる．
#https://keras.io/ja/models/about-keras-models/


def Readdata(filename,Inputhead):
    df = pd.read_csv(filename,encoding="utf-8")#データ読み込み
    datas = df[Inputhead]
    label_datas = df["Labeldata"]

    def Append(datas):

        textdatas = []
        for data in datas:
            text = np.array([])
            """日本語用"""
            #tagger= MeCab.Tagger("-Owakati")
            #data=tagger.parse(data)
            data_list = (str(data).replace('\n','')).split()
            #print(data_list)
            data_length = len(data_list)
            for i, word in enumerate(data_list):
                if (i == 0):
                    #text = np.append(text, "<BOS>")
                    text = np.append(text, word)
                elif (i >= data_length - 1):
                    text = np.append(text, word)
                    #text = np.append(text, "<EOS>")
                else:
                    text = np.append(text, word)
            textdatas.append(text)
        return np.array(textdatas)

    datas = Append(datas)
    label_datas = Append(label_datas)

    return datas, label_datas


#target も作成できるようにする
def OnehotMakedata(filedatalist,picklefilename,max_sentence_length = 0):

    for word in filedatalist:
        if max_sentence_length < len(word):
            max_sentence_length = len(word)
    sentence_length = max_sentence_length

    print(sentence_length)
    c_f = {}  # {}で辞書オブジェクトを作成する c_fはindexの場所を指す
    depth = 250  # Vocablaryによるが#depth位以下の単語を削る

    "Vocaburary辞書を作成する"

    for data in filedatalist:
        for word in data:
            if c_f.get(word) is None:  # 要素がないなら作成する. c番目の値を0にする
                # https: // note.nkmk.me / python - dict - list - values /
                c_f[word] = 0
            c_f[word] += 1  # 文字列を多くする.
    # sorted タプルをソートできる. 数が多い順に並び替えて表示
    #for e, (c, f) in enumerate(sorted(c_f.items(), key=lambda x: x[1] * -1)):
    #    print(e, c, f)
    c_i = {c: e for e, (c, f) in enumerate(sorted(c_f.items(), key=lambda x: x[1] * -1)[:depth])}
    open(picklefilename, "wb").write(pickle.dumps(c_i))


    #辞書ロードし，それをOnehotに変更する.Readdata
    onehot_vector = []
    Next_onehot_vector = []

    for i,data in enumerate(filedatalist):
        xd = [[0.] * len(c_i) for _ in range(sentence_length)]
        Next_target =  [[0.] * len(c_i) for _ in range(sentence_length)]
        for l,word in enumerate(data):
            xd[l][c_i[word]] = 1.
            if l > 0 :
                Next_target[l - 1][c_i[word]] = 1.
            elif l >= len(data) :
                Next_target[l][c_i["<EOS>"]] = 1.

        onehot_vector.append(np.array(list(xd)))
        Next_onehot_vector.append(np.array(list(Next_target)))

    #print("shapeのデータ",np.array(onehot_vector).shape)

    return np.array(onehot_vector),np.array(Next_onehot_vector)



def Makevocab(picklefilename,outputfilename):
    c_i = pickle.load(open(picklefilename, "rb"))

    print("label")
    print(c_i)
    print(len(c_i))
    with open(outputfilename,"w") as f:
        for word in c_i:
            f.write(word+"\n")









if __name__ == '__main__':
    traindata_filename = "/Users/pro11/Desktop/yota/Master_thesis/source/NoiseMakeData/Dataset/"+sys.argv[1]
    train_V_picklename = "Vocabulary.pkl"
    print("data Download")
    train_data, label_datas = Readdata(traindata_filename,sys.argv[2])
    if sys.argv[2] == "Input":
        label_V_picklename = "Vocabularytrain.pkl"
        train_ohl_datas, Next_ohl_target = OnehotMakedata(label_datas, label_V_picklename)
        Makevocab(label_V_picklename,"./Dataset/Vocab.out")

    print("Onehot Vector")
    train_oh_datas, Next_oh_target = OnehotMakedata(train_data, train_V_picklename)
    Makevocab(train_V_picklename,"./Dataset/Vocab"+sys.argv[2]+".in")





    # 未学習のデータでテスト
    #x_test = np.array([np.sin([[p] for p in np.arange(0, 0.8, 0.1)] + aa) for aa in np.arange(0, 1.0, 0.1)])
    #print(model.evaluate(x_test, y_test, batch_size=32))
    # 未学習のデータで生成
    #predicted = model.predict(x_test, batch_size=32)
