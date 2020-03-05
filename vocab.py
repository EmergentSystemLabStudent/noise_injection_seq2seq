import numpy as np
import pickle
import sys
import pandas as pd


def Readdata(filename, inputhead):
    df = pd.read_csv(filename, encoding="utf-8")
    datas = df[inputhead]
    label_datas = df["labeldata"]

    def Append(datas):
        textdatas = []
        for data in datas:
            text = np.array([])
            data_list = (str(data).replace("\n", "")).split()
            data_length = len(data_list)
            for i, word in enumerate(data_list):
                if i == 0:
                    text = np.append(text, word)
                elif i >= data_length - 1:
                    text = np.append(text, word)
                else:
                    text = np.append(text, word)
            textdatas.append(text)
        return np.array(textdatas)

    datas = Append(datas)
    label_datas = Append(label_datas)

    return datas, label_datas


def SentenceLength(filedatalist):
    max_sentence_length = 0
    for sentence in filedatalist:
        if max_sentence_length < len(sentence):
            max_sentence_length = len(sentence)
    return max_sentence_length


def OnehotMakedata(filedatalist, picklefilename):
    c_f = {}
    depth = 250
    for sentence in filedatalist:
        for symbol in sentence:
            if c_f.get(symbol) is None:
                c_f[symbol] = 0
            c_f[symbol] += 1
    c_i = {
        c: e
        for e, (c, f) in enumerate(sorted(c_f.items(), key=lambda x: x[1] * -1)[:depth])
    }
    open(picklefilename, "wb").write(pickle.dumps(c_i))


def Makevocab(picklefilename, outputfilename):
    c_i = pickle.load(open(picklefilename, "rb"))
    print("label")
    print(c_i)
    print(len(c_i))
    with open(outputfilename, "w") as f:
        for word in c_i:
            f.write(word + "\n")


if __name__ == "__main__":
    data_filename = "./OriginalDataset/" + sys.argv[1]
    datas, label_datas = Readdata(data_filename, sys.argv[2])
    print("sentence_length:" + str(SentenceLength(data_filename)))
    picklename = "Vocabulary.pkl"
    OnehotMakedata(datas, picklename)
    if sys.argv[2] == "label":
        Makevocab(picklename, "./Dataset/Vocab.out")
    else:
        Makevocab(picklename, "./Dataset/Vocab" + sys.argv[2] + ".in")
