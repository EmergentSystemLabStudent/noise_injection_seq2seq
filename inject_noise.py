import numpy as np
import  pronouncing
import pandas as pd
import sys
from tqdm import tqdm 
import os

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

d = {s: v for s,v in enumerate(phenome) }
cmudict = {"Softner":"S AO F AX N AX"}

def load_data(filename):
    df = pd.read_csv(filename,encoding="cp932")
    data = df["data"]
    label = df["labeldata"]
    return data,label

def random_phoneme():
    index = int(np.random.randint(0, len(phenome), 1))
    return d[index]

def Insert():
    return random_phoneme()

def Substitution(ph,rho):
    L = len(phenome)
    if (np.random.binomial(1,rho*L/((1.0-2.0*rho)*(L-1)))):
        s_ph = random_phoneme()
    else:
        s_ph = ph
    return s_ph

def adjust_sentence(sentence):
    adj_sentence = []
    for _, word in enumerate(sentence.split(" ")):
        if "_" in word:
            splited_words = word.split("_")
            for w in splited_words:
                adj_sentence.append(w)
        elif "nearby" in word:
            splited_words = ["near","by"]
            for w in splited_words:
                adj_sentence.append(w)
        elif "." in word:
            continue
        else:
            adj_sentence.append(word)
    return adj_sentence

def get_phenome_Sentence(adj_sentence):
    phenomeSentence = []
    for _,word in enumerate(adj_sentence):
        ph = pronouncing.phones_for_word(word)
        if not ph:
            print("--------------------",word,"--------------------")
            print("error")
            exit()
        else:
            ph = ph[0].split()
        phenomeSentence.extend(ph)
    return phenomeSentence

def edit_phenome_sentence(phenomeSentence,rho):
    edited_phenome_sentence=[]
    for _, phletter in enumerate(phenomeSentence):
        while True:
            if(np.random.binomial(1, rho)):
                edited_phenome_sentence.append(Insert())
            else:
                break       
        if(np.random.binomial(1, (1-2*rho)/(1-rho))):
            edited_phenome_sentence.append(Substitution(phletter,rho))
    return edited_phenome_sentence

def main():
    edited_dir_path = sys.argv[1]
    original_dir_path = sys.argv[2]
    original_filename = sys.argv[3]
    rho=float(sys.argv[4])
    data_filepath = original_dir_path + original_filename +"data.csv" 

    sentences,labels = load_data(data_filepath)

    str_noiselevel = "rho="+str(rho)
    print(str_noiselevel)
    
    phenome_data = []
    noisy_data = []
    for j,sentence in enumerate(tqdm(sentences)):
        adj_sentence = adjust_sentence(sentence)
        phenomeSentence = get_phenome_Sentence(adj_sentence)
        phenome_data.append(phenomeSentence)
        edited_phenome_sentence = edit_phenome_sentence(phenomeSentence,rho)
        noisy_data.append(edited_phenome_sentence)

    os.mkdir(edited_dir_path+str_noiselevel)
    with open(edited_dir_path+str_noiselevel+"/"+"original_sentence_"+original_filename.replace(".csv","")+".in",mode="w") as f:
        for i, sentence in enumerate(sentences):
            f.write(sentence)
            f.write("\n")

    with open(edited_dir_path+str_noiselevel+"/"+"phoneme_"+original_filename.replace(".csv","")+".in",mode="w") as f:
        for i, phenomeSentence in enumerate(phenome_data):
            f.write(" ".join(phenomeSentence))
            f.write("\n")

    with open(edited_dir_path+str_noiselevel+"/"+"edited_phoneme_"+original_filename.replace(".csv","")+".in",mode="w") as f:
        for i, noisySentence in enumerate(noisy_data):
            f.write(" ".join(noisySentence))
            f.write("\n")

    with open(edited_dir_path+str_noiselevel+"/"+"label_"+original_filename.replace(".csv","")+".out",mode="w") as f:
        for i, label in enumerate(labels):
            f.write(label)
            f.write("\n")

    with open(edited_dir_path+str_noiselevel+"/"+original_filename,mode="w") as f:
        f.writelines("original_sentence,phoneme,edited_phoneme,label\n")
        for i, (train_data, phenomeSentence, noisySentence, labelSentence) in enumerate(
                zip(sentences, phenome_data, noisy_data, labels)):
            f.write(train_data+","+" ".join(phenomeSentence)+","+" ".join(noisySentence)+","+labelSentence)
            f.write("\n")

if __name__ == '__main__':
    main()
    #sys.argv[1]:edited data directory path
    #sys.argv[2]:original data directory path
    #sys.argv[3]:train/test/dev
    #sys.argv[4]:noise level

    