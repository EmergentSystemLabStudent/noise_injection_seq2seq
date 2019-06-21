from jiwer import wer
import pandas as pd
import sys
if __name__ == '__main__':
    dir = sys.argv[1]
    df = pd.read_csv(dir+"SpeechRecognitionResults.csv")
    for index,row in df.iterrows():
        s1=row.original_sentence
        s1=s1.replace("_"," ")
        s1=s1.replace("."," ")
        s2=row.google_word
        print(index,wer(s1,s2))

