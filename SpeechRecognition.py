import speech_recognition
import sys
import pandas as pd
import os.path
import pronouncing
import glob
import re

def SpeechRecognition(filename):

    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(filename) as source:
        audio = r.record(source)

    google_result=r.recognize_google(audio, show_all=True)

    units = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

    #print("Google_result:",google_result["alternative"][0]['transcript'])
    
    google_phoneme = []
    for word in (google_result["alternative"][0]['transcript']).split():
            #print(word)
            ph = pronouncing.phones_for_word(str(word))
            if not ph:
                word =re.sub(re.compile("[!-/:-@[-`{-~]"), '', word)
                #print("--------------------Word :", word, "--------------------")
                for phoneme in str(word):
                    #print(phoneme.isdecimal())
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
                        #print(ph)
                    google_phoneme.extend(ph)
            else:
                ph = ph[0].split()
                #print(ph)
                google_phoneme.extend(ph)
    #print("Google_phoneme_result:",google_phoneme)


    sphinx_result=r.recognize_sphinx(audio, show_all=True)
    #print("Sphinx_result:",sphinx_result.hyp().hypstr)                
    
    sphinx_phoneme = []
    for word in (sphinx_result.hyp().hypstr).split():
            #print(word)
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
                        #print(ph)
                    sphinx_phoneme.extend(ph)
            else:
                ph = ph[0].split()
                #print(ph)
                sphinx_phoneme.extend(ph)
    #print("Sphinx_phoneme_result:",sphinx_phoneme)
    
   
    result = [filename,google_result["alternative"][0]['transcript']," ".join(google_phoneme),sphinx_result.hyp().hypstr," ".join(sphinx_phoneme)]
    return result

if __name__ == '__main__':
    dir = sys.argv[1]
    out_dir = sys.argv[2]
    fitsf=sorted(glob.glob(dir+"*.wav"))
    results = []
    for _,filename in enumerate(fitsf):
        print(filename)
        result=SpeechRecognition(filename)
        results.append([result[0],result[1],result[2],result[3],result[4]])
    df1 = pd.DataFrame(results,columns=["filename","google_word","google_phoneme","sphinx_word","sphinx_phoneme"])
    df2 = pd.read_csv("GPSRsentence_list.csv")
    df = pd.merge(df1,df2,left_index=True,right_index=True)
    df.to_csv(out_dir+"SpeechRecognitionResults.csv",columns=["filename","original_sentence","google_word","google_phoneme","sphinx_word","sphinx_phoneme"] )


