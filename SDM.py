import numpy as np
import  pronouncing
import pandas as pd
from datetime import datetime
import sys

#probs = [[1/20,9/10,1/20],[2/20,16/20,2/20],[4/20,12/20,4/20],[6/20,8/20,6/20],[8/20,4/20,8/20],[10/20,6/20,4/20],[4/20,6/20,10/20],[14/20,4/20,2/20],[2/20,4/20,14/20]]
probs = [[1/20,9/10,1/20]] 

phenome = ["AA",
"AA0",
"AA1",
"AA2",
"AE",
"AE0",
"AE1",
"AE2",
"AH",
"AH0",
"AH1",
"AH2",
"AO",
"AO0",
"AO1",
"AO2",
"AW",
"AW0",
"AW1",
"AW2",
"AY",
"AY0",
"AY1",
"AY2",
"B",
"CH",
"D",
"DH",
"EH",
"EH0",
"EH1",
"EH2",
"ER",
"ER0",
"ER1",
"ER2",
"EY",
"EY0",
"EY1",
"EY2",
"F",
"G",
"HH",
"IH",
"IH0",
"IH1",
"IH2",
"IY",
"IY0",
"IY1",
"IY2",
"JH",
"K",
"L",
"M",
"N",
"NG",
"OW",
"OW0",
"OW1",
"OW2",
"OY",
"OY0",
"OY1",
"OY2",
"P",
"R",
"S",
"SH",
"T",
"TH",
"UH",
"UH0",
"UH1",
"UH2",
"UW",
"UW0",
"UW1",
"UW2",
"V",
"W",
"Y",
"Z",
"ZH"]

def ReadFile(filename):
    df = pd.read_csv(filename,encoding="cp932")
    Datas = df["data"]
    Labels = df["labeldata"]
    return Datas,Labels

d = {s: v for s,v in enumerate(phenome) }

cmudict = {"Softner":"S AO F AX N AX"}

def Insert(word):
    index = int(np.random.randint(0, len(phenome), 1))
    Nosiyword = d[index]
    return Nosiyword

def Substitution(word):
    B = 30
    L = len(phenome)
    Same_PI = (B - 1)/ B + 1/(B*L)
    q = 1/(B*L)
    if (np.random.choice([True]+[False]*(L - 1), p=[Same_PI]+[q]*(L - 1) ) == True):
        Nosiyword = word
    else:
        index=int(np.random.randint(0, len(phenome), 1))
        Nosiyword = d[index]
    return Nosiyword

#def Delete(word):

#def Stop():


if __name__ == '__main__':
    if not sys.argv[1]:
        print("error")
    data_filename = "./OriginalDataset/"+sys.argv[1]

    trainingDatas,labelDatas = ReadFile(data_filename)

    for PI,PS,PD in probs:
        print("PI,PS,PD",PI,PS,PD)
        phenomeDatas = []
        noisydata = []

        for j,sentence in enumerate(trainingDatas):
            adj_sentence = []
            for i, word in enumerate(sentence.split(" ")):
                if "_" in word:
                    splitWord = word.split("_")
                    for data in splitWord:
                        adj_sentence.append(data)
                elif "nearby" in word:
                    splitWord = ["near","by"]
                    for data in splitWord:
                        adj_sentence.append(data)
                elif "." in word:
                    continue
                else:
                    adj_sentence.append(word)

            phenomeSentence = []
            y = []
            for j,word in enumerate(adj_sentence):
                ph = pronouncing.phones_for_word(word)
                if not ph:
                    print("--------------------",word,"--------------------")
                    print("error")
                    exit()
                else:
                    ph = ph[0].split()
                phenomeSentence.extend(ph)

                for i, phletter in enumerate(ph):
                    if (np.random.choice(["Insert","Stop"],p=[PI,1 - PI]) == "Insert"):
                        y.append(Insert(phletter))
                        while True:
                            if(np.random.choice(["Insert", "Stop"], p=[PI, 1 - PI]) == "Insert"):
                                y.append(Insert(phletter))
                            else:
                                break
                    #Stop()
                    operation = np.random.choice(["Substitution", "Delete"], p=[PS/(PS+PD), PD/(PS+PD)])
                    if(operation =="Substitution"):
                        y.append(Substitution(phletter))
                    #elif(operation =="Delete"):
                        #Delete(phletter)

            noisydata.append(y)
            phenomeDatas.append(phenomeSentence)

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+sys.argv[1],
                      mode="w") as f:
                f.writelines("Input,phonemelabel,Noisylabel,Labeldata\n")
                for i, (train_data, phenomeSentence, noisySentence, labelSentence) in enumerate(
                        zip(trainingDatas, phenomeDatas, noisydata, labelDatas)):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(train_data+","+" ".join(phenomeSentence)+","+" ".join(noisySentence)+","+labelSentence)
                    f.write("\n")

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"Input"+str(sys.argv[1]).replace(".csv","")+".in",
                      mode="w") as f:
                for i, train_data in enumerate(trainingDatas):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(train_data)
                    f.write("\n")

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"phoneme"+str(sys.argv[1]).replace(".csv","")+".in",
                      mode="w") as f:
                for i, phenomeSentence in enumerate(phenomeDatas):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(" ".join(phenomeSentence))
                    f.write("\n")

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"noisy"+str(sys.argv[1]).replace(".csv","")+".in",
                          mode="w") as f:
                for i, noisySentence in enumerate(noisydata):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(" ".join(noisySentence))
                    f.write("\n")

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"label"+str(sys.argv[1]).replace(".csv","")+".out",mode="w") as f:
                for i, labelSentence in enumerate(labelDatas):
                    f.write(labelSentence)
                    f.write("\n")
