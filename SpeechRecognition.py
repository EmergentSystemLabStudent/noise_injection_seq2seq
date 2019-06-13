# coding=utf-8

# write code...
import speech_recognition
import sys
import pandas as pd
import os.path
import pronouncing
import glob
import re

#dir ="WANGDATA/"
dir ="KOBAYASHIDATA/"

def format_text(text):
    '''
    MeCabに入れる前のツイートの整形方法例
    '''

    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub('RT', "", text)
    text=re.sub('お気に入り', "", text)
    text=re.sub('まとめ', "", text)
    text=re.sub(r'[!-~]', "", text)#半角記号,数字,英字
    text=re.sub(r'[︰-＠]', "", text)#全角記号
    text=re.sub('\n', " ", text)#改行文字

    return text

def MakeRecodedata(filename):
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(filename) as source:
        audio = r.record(source)

    google_result=r.recognize_google(audio, show_all=True)
    sphinx_result=r.recognize_sphinx(audio, show_all=True)


    units = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

    print("Google_result:",google_result["alternative"][0]['transcript'])
    print("Sphinx_result:",sphinx_result.hyp().hypstr)

    google_phoneme = []

    for word in (google_result["alternative"][0]['transcript']).split():
            print(word)
            #word =format_text(word)
            #print(word)
            ph = pronouncing.phones_for_word(str(word))
            if not ph:
                word =re.sub(re.compile("[!-/:-@[-`{-~]"), '', word)
                print("--------------------Word :", word, "--------------------")
                for phoneme in str(word):
                    print(phoneme.isdecimal())
                    if phoneme.isdecimal():
                        phoneme = units[phoneme]
                    elif phoneme.find(".") > -1:
                        continue

                    ph = pronouncing.phones_for_word(phoneme)
                    if not ph:
                        print("error")
                        exit()
                    else :
                        ph = ph[0].split()
                        print(ph)
                    google_phoneme.extend(ph)
            else:
                ph = ph[0].split()
                print(ph)
                google_phoneme.extend(ph)

    sphinx_phoneme = []
    for word in (sphinx_result.hyp().hypstr).split():
            print(word)
            #word =format_text(word)
            #print(word)
            ph = pronouncing.phones_for_word(str(word))
            if not ph:
                print("--------------------Word :", word, "--------------------")
                for phoneme in str(word):
                    print(phoneme.isdecimal())
                    if phoneme.isdecimal():
                        phoneme = units[phoneme]
                    ph = pronouncing.phones_for_word(phoneme)
                    if not ph:
                        print("error")
                        exit()
                    else :
                        ph = ph[0].split()
                        print(ph)
                    sphinx_phoneme.extend(ph)
            else:
                ph = ph[0].split()
                print(ph)
                sphinx_phoneme.extend(ph)



    #googlecloud_result=r.recognize_google_cloud(audio)
    print("Google_phneme_result:",google_phoneme)
    print("Sphinx_phneme_result:",sphinx_phoneme)

    frame =pd.DataFrame([[filename,google_result["alternative"][0]['transcript']," ".join(google_phoneme),sphinx_result.hyp().hypstr," ".join(sphinx_phoneme)]],columns=["Data","google_result","google_phoneme","sphinx_result","sphinx_phoneme"])



    """
    ph = pronouncing.phones_for_word(word)
                if not ph:
                    print("--------------------",word,"--------------------")
                    print("error")
                    exit()
                else:
                    ph = ph[0].split()
    """
    path =dir+"google_Wordresultdata.csv"
    df = frame["google_result"].to_csv(path,index=False,mode='a')

    path =dir+"google_phonemeresultdata.csv"
    df = frame["google_phoneme"].to_csv(path,index=False,mode='a')


    path =dir+"sphinx_wordresultdata.csv"
    df = frame["sphinx_result"].to_csv(path,index=False,mode='a')


    path =dir+"sphinx_phonemeresultdata.csv"
    df = frame["sphinx_phoneme"].to_csv(path,index=False,mode='a')

    path =dir+"checkdata.csv"
    frame =pd.DataFrame([[filename,google_result["alternative"][0]['transcript'],sphinx_result.hyp().hypstr]],columns=["Data","google_result","sphinx_result"])
    frame.to_csv(path, index=False, mode='a',header=False)


    path =dir+"RecognitionResult.csv"
    if not os.path.exists(path):
        df = frame.to_csv(path,index=False,mode='w')
    else:
        df = frame.to_csv(path, index=False, mode='a',header=False)

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def main():

    fitsf=sorted(glob.glob(dir+"/ID*.wav"), key=numericalSort)
    for filename in fitsf:
        MakeRecodedata(filename)

if __name__ == '__main__':
    main()


#to_csv()
