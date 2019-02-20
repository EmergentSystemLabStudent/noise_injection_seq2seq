import pronouncing

filename = "cat1Sentences.en.txt"

for it  in [item.strip('\n')     for item     in open(filename,   'r').readlines()]: #改行で配列に入れる
    if it  == '':
        continue
    if it[0] == '#':
        continue
    adj_sentence = []
    for i, word in enumerate(it.split(" ")):
        if word in "_":
            word = word.split("_")
            for data in word:
                adj_sentence.append(word)
        else:
            adj_sentence.append(word)
        print(adj_sentence)
        for i,word in enumerate(adj_sentence):
            if it  == '':
                    continue
            #まず挿入かどうか
            print(word)
            ph = (pronouncing.phones_for_word(word)[0]).split()
            print(ph)
