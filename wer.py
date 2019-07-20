from jiwer import wer
import pandas as pd
import sys
if __name__ == '__main__':
    dir = sys.argv[1]
    df = pd.read_csv(dir+"SpeechRecognitionResults.csv")
    sumg=0
    sums=0
    for index,row in df.iterrows():
        s1=row.original_sentence
        s1=s1.replace("_"," ")
        s1=s1.replace("."," ")
        s2=row.google_word
        s3=row.sphinx_word
        wg=wer(s1,s2)
        ws=wer(s1,s3)
        print(index,wg,ws)
        sumg+=wg
        sums+=ws
    print("avg",sumg/100.0,sums/100.0)
