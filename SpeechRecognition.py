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

    """
    sphinx_result=r.recognize_sphinx(audio, show_all=True)
    print("Sphinx_result:",sphinx_result.hyp().hypstr)                
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
    print("Sphinx_phneme_result:",sphinx_phoneme)
"""

    
    result = [filename,google_result["alternative"][0]['transcript']," ".join(google_phoneme)]
    return result

    #path =dir+"google_Wordresultdata.csv"
    #df = frame["google_result"].to_csv(path,index=False,mode='a')

    #path =dir+"google_phonemeresultdata.csv"
    #df = frame["google_phoneme"].to_csv(path,index=False,mode='a')

    #path =dir+"sphinx_wordresultdata.csv"
    #df = frame["sphinx_result"].to_csv(path,index=False,mode='a')

    #path =dir+"sphinx_phonemeresultdata.csv"
    #df = frame["sphinx_phoneme"].to_csv(path,index=False,mode='a')

    #path =dir+"checkdata.csv"
    #frame =pd.DataFrame([[filename,google_result["alternative"][0]['transcript'],sphinx_result.hyp().hypstr]],columns=["Data","google_result","sphinx_result"])
    #frame.to_csv(path, index=False, mode='a',header=False)


    #path =dir+"RecognitionResult.csv"
    #if not os.path.exists(path):
    #    df = frame.to_csv(path,index=False,mode='w')
    #else:
    #    df = frame.to_csv(path, index=False, mode='a',header=False)


if __name__ == '__main__':
    dir = sys.argv[1]
    
    fitsf=sorted(glob.glob(dir+"*.wav"))
    results = []
    for filename in fitsf:
        print(filename)
        result=SpeechRecognition(filename)
        results.append(result)
    df = pd.DataFrame(results,columns=["filename","google_word","google_phoneme"])
    df.to_csv(dir+"SpeechRecognitionResults.csv",index=False)

