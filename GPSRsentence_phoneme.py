import pandas as pd
import pronouncing

df = pd.read_csv("./GPSRsentence_list.csv")
for index,row in df.iterrows():
    phoneme = ""
    for word in row.original_sentence.replace("_"," ").split(" "):
        ph = pronouncing.phones_for_word(str(word))
        if ph:
            phoneme = phoneme + ph[0]+" "
    print(phoneme)

