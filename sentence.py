import numpy as np
import  pronouncing
from copy import copy
from random_phoneme import get_random_phoneme, get_number_phoneme

class words_sentence(object):
    def __init__(self,original_string):
        self.words=self.split_str(original_string)       
    def split_str(self,str):
        words = []
        for _, word in enumerate(str.split(" ")):
            if "_" in word:
                splited_words = word.split("_")
                for w in splited_words:
                    words.append(w)
            elif "nearby" in word:
                splited_words = ["near","by"]
                for w in splited_words:
                    words.append(w)
            elif "." in word:
                continue
            else:
                words.append(word)
        return words
    def get_words(self):
        return self.words

class phonemes_sentence(object):
    def __init__(self,words):
        self.phonemes = self.convert_words_to_phonemes(words)
        self.noise = False

    def convert_words_to_phonemes(self,words):
        phonemes = []
        for _,word in enumerate(words):
            ph = pronouncing.phones_for_word(word)
            if not ph:
                print("--------------------",word,"--------------------")
                print("error")
                exit()
            else:
                ph = ph[0].split()
            phonemes.extend(ph)
        return phonemes

    def inject_noise(self,rho):
        self.noise = True
        temp_phonemes = [] 
        for _, phoneme in enumerate(self.phonemes):
            while True:
                if(np.random.binomial(1, rho)):
                    # insert
                    temp_phonemes.append(get_random_phoneme())                  
                else:
                    break       
            if(np.random.binomial(1, (1-2*rho)/(1-rho))):
                # substitution
                temp_phonemes.append(self.substitution_phoneme(phoneme,rho))
                
        self.phonemes = temp_phonemes  
    
    def substitution_phoneme(self,phoneme,rho):
        L = get_number_phoneme()
        if (np.random.binomial(1,rho*L/((1.0-2.0*rho)*(L-1)))):
            s_ph = get_random_phoneme()
        else:
            s_ph = phoneme
        return s_ph
    
class sentence:  
    def __init__(self,original_string,rho):
        self.words_sentence = words_sentence(original_string)
        self.phonemes_sentence = phonemes_sentence(self.words_sentence.get_words())
        self.edited_phonemes_sentence = copy(self.phonemes_sentence)
        self.edited_phonemes_sentence.inject_noise(rho)
        
