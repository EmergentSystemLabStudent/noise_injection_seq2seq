import matplotlib.pylab as plt
import numpy as np
import datetime
import pickle
import os
import glob
import sys
import math
import pandas as pd

def Readdata(filename,Inputhead):
    df = pd.read_csv(filename,encoding="utf-8")
    datas = df[Inputhead]
    label_datas = df["Labeldata"]

    def Append(datas):
        textdatas = []
        for data in datas:
            text = np.array([])
            data_list = (str(data).replace('\n','')).split()
            data_length = len(data_list)
            for i, word in enumerate(data_list):
                if (i == 0):
                    text = np.append(text, word)
                elif (i >= data_length - 1):
                    text = np.append(text, word)
                else:
                    text = np.append(text, word)
            textdatas.append(text)
        return np.array(textdatas)

    datas = Append(datas)
    label_datas = Append(label_datas)

    return datas, label_datas


def OnehotMakedata(filedatalist,picklefilename,max_sentence_length = 0):
    for word in filedatalist:
        if max_sentence_length < len(word):
            max_sentence_length = len(word)
    sentence_length = max_sentence_length

    print(sentence_length)
    c_f = {}  
    depth = 250  

    for data in filedatalist:
        for word in data:
            if c_f.get(word) is None:
                c_f[word] = 0
            c_f[word] += 1
    c_i = {c : e for e, (c, f) in enumerate(sorted(c_f.items(), key=lambda x: x[1] * -1)[:depth])}
    open(picklefilename, "wb").write(pickle.dumps(c_i))

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
