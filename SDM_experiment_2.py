# coding=utf-8

import transitions
from transitions import Machine
import numpy as np
import  pronouncing
import pandas as pd
from datetime import datetime
import sys
import math

"""

"""


#状態の定義
states=['Ti', 'Si']

#遷移の定義
# trigger：遷移の引き金になるイベント、source：トリガーイベントを受ける状態、dest：トリガーイベントを受けた後の状態
# before：遷移前に実施されるコールバック、after：遷移後に実施されるコールバック
#線の定義
#.add_transitionで定義できる


transitions = [
    {'trigger': 'Delete', 'source': 'Ti', 'dest': 'Si','before': 'action_Delete'},
    {'trigger': 'Insert', 'source': 'Si', 'dest': 'Si','before': 'action_Insert'},
    {'trigger': 'SameSubstitution', 'source': 'Ti', 'dest': 'Si','before': 'action_SameSubstitution'},
    {'trigger': 'Substitution', 'source': 'Ti', 'dest': 'Si','before': 'action_Substitution'},
    {'trigger': 'SubStop', 'source': 'Si', 'dest': 'Ti', 'before': 'action_Stop'}
]

#遷移「前」の状態(transitionsに定義したsource)で実施されます。一方で'after'にコールバックを指定した場合は遷移「後」の状態


prods = [0.05,0.1,0.2,0.3]



def ReadFile(filename):
    df = pd.read_csv(filename,encoding="cp932")#データ読み込み
    TrainDatas = df["data"]
    LabelDatas = df["labeldata"]
    return TrainDatas,LabelDatas


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
"F","G","HH","IH",
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

d = {s: v for s,v in enumerate(phenome) }

cmudict = {"Softner":"S AO F AX N AX"}

class Matter(object):
    def action_Delete(self):
        #print("*** action_Delete ***")
        #文字
        pass
    def action_Insert(self):
        #print("*** action_Insert ***")
        #同じ文字をInsertするかどうか
        pass
    def action_SameSubstitution(self):
        pass

    def action_Substitution(self):
        #print("*** action_Substitution ***")
        pass
    def action_Stop(self):
        #print("*** action_Stop ***")
        pass



lump = Matter()
machine = Machine(model=lump, states=states, transitions=transitions, initial='Si')
#http://www.speech.cs.cmu.edu/cgi-bin/cmudict
#https://pronouncing.readthedocs.io/en/latest/tutorial.html
#補助シンボルなし


def Insert(word):
    lump.Insert()
    #print("Insert")
    index = int(np.random.randint(0, len(phenome), 1))
    Nosiyword = d[index]
    return Nosiyword

def SameSubstitution(word):
    lump.SameSubstitution()
    Nosiyword = word
    return Nosiyword

def Substitution(word):
    lump.Substitution()
    #B = 30
    #L = len(phenome)
    #Same_PI = (B - 1)/ B + 1/(B*L)
    #q = 1/(B*L)
    #print("Substitution")
    index=int(np.random.randint(0, len(phenome), 1))
    Nosiyword = d[index]
    return Nosiyword

def Delete(word):
    lump.Delete()
    #print("Delete")

def Stop():
    lump.SubStop()

if __name__ == '__main__':
    if not sys.argv[1]:
        print("error")
    traindata_filename = "./OriginDataset/"+sys.argv[1]

    trainingDatas,labelDatas = ReadFile(traindata_filename)

    for v in prods:
        #この場合は雑音が偏る場合
        PI = round(1.0 - 3.0*v, 2)
        PD = v
        PS = v
        PS_S = v

        print("PI,PS,PS_SAME,PD",PI,PS,PS_S,PD)
        phenomeDatas = []
        Noisydata = []

        for j,sentence in enumerate(trainingDatas):
            adj_sentence = []
            phenomeSentence = []
            y = []
            for i, word in enumerate(sentence.split(" ")):
                if "_" in word:
                    splitWord = word.split("_")
                    for data in splitWord:
                        adj_sentence.append(data)
                elif "neayby" in word:
                    splitWord = ["near","by"]
                    for data in splitWord:
                        adj_sentence.append(data)
                elif "." in word:
                    continue
                else:
                    adj_sentence.append(word)
            adj_sentence = [x for x in adj_sentence if x]
            #print(adj_sentence)

            for j,word in enumerate(adj_sentence):
                #まず挿入かどうか
                ph = pronouncing.phones_for_word(word)
                if not ph:
                    print("--------------------",word,"--------------------")
                    print("error")
                    exit()
                else:
                    ph = ph[0].split()
                phenomeSentence.extend(ph)

                for i, phletter in enumerate(ph):
                    phletter = phletter

                    if (np.random.choice([True,False],p=[PI,1 - PI]) == True):
                        #print("Insert")
                        y.append(Insert(phletter))#関数
                        while True:
                            if(np.random.choice([True, False], p=[PI, 1 - PI]) == True):
                                #print("Insert")
                                y.append(Insert(phletter))  # 関数
                            else:
                                break
                    Stop()
                    state = np.random.choice(["Substitution","Delete","SameSubstitution"], p=[PS/(PS+PD+PS_S), PD/(PS+PD+PS_S),PS_S/(PS+PD+PS_S)])
                    if(state =="Substitution"):
                        y.append(Substitution(phletter))
                    elif(state =="SameSubstitution"):
                        y.append(SameSubstitution(phletter))
                    elif(state =="Delete"):
                        Delete(phletter)
            #print("y:",j,y)
            #print("phonime:",j,phenomeSentence)
            Noisydata.append(y)
            phenomeDatas.append(phenomeSentence)

            #traindata,phonemelabel.labldata
            now = datetime.now()
            nowtime = str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)

            #元の現状

            """
            with open("./Result"+str(sys.argv[1]).replace(".csv","")+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"PS_S"+str(PS_S)+sys.argv[1],
                      mode="w") as f:
                f.writelines("Input,phonemelabel,Noisylabel,Labeldata\n")
                for i, (train_data, phenomeSentence, NoisySentence, labelSentence) in enumerate(
                        zip(trainingDatas, phenomeDatas, Noisydata, labelDatas)):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(train_data+","+" ".join(phenomeSentence)+","+" ".join(NoisySentence)+","+labelSentence)
                    f.write("\n")
            """
            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"PS_S"+str(PS_S)+sys.argv[1],
                      mode="w") as f:
                f.writelines("Input,phonemelabel,Noisylabel,Labeldata\n")
                for i, (train_data, phenomeSentence, NoisySentence, labelSentence) in enumerate(
                        zip(trainingDatas, phenomeDatas, Noisydata, labelDatas)):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(train_data+","+" ".join(phenomeSentence)+","+" ".join(NoisySentence)+","+labelSentence)
                    f.write("\n")


            #in と out
            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"PS_S"+str(PS_S)+"Input"+str(sys.argv[1]).replace(".csv","")+".in",
                      mode="w") as f:
                for i, train_data in enumerate(trainingDatas):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(train_data)
                    f.write("\n")

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"PS_S"+str(PS_S)+"phoneme"+str(sys.argv[1]).replace(".csv","")+".in",
                      mode="w") as f:
                for i, phenomeSentence in enumerate(phenomeDatas):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(" ".join(phenomeSentence))
                    f.write("\n")

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"PS_S"+str(PS_S)+"Noisy"+str(sys.argv[1]).replace(".csv","")+".in",
                          mode="w") as f:
                for i, NoisySentence in enumerate(Noisydata):
                    #print("PhonemeSentence:"," ".join(phenomeSentence),"NoisyData:"," ".join(NoisySentence))
                    f.write(" ".join(NoisySentence))
                    f.write("\n")

            with open("./Dataset"+"/"+"PI_"+str(PI)+"PS_"+str(PS)+"PD_"+str(PD)+"PS_S"+str(PS_S)+"label"+str(sys.argv[1]).replace(".csv","")+".out",mode="w") as f:
                for i, labelSentence in enumerate(labelDatas):
                    f.write(labelSentence)
                    f.write("\n")
