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
        s1=s1.replace("  "," ")
        s1=s1.rstrip(" ")
        s1=s1.lower()
        s2=row.google_word
        s3=row.sphinx_word
        print(index)
        print(s1)
        print(s2)
        print(s3)
        print(s1==s2)
        if(s1==s2):
            sumg=sumg+1
        if(s1==s3):
            sums=sums+1

    print("Google:",sumg/100.0," , Sphinx:",sums/100.0)
