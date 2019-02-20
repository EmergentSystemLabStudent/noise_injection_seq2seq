#!/usr/bin/python
# -*- coding: utf-8 -*-
#######################################################
# GPSR sentence generator
# version: 15.05
#
# Programmed by:
# Tijn van der Zant, Komei Sugiura
# email: tijn@ieee.org, komei.sugiura@gmail.com
#
#######################################################

# imports
import random
import sys
import copy
import os
import pandas as pd
import string
import base64
import urllib2
import json
import wave

# service URL
tts_url ='http://rospeex.ucri.jgn-x.jp/nauth_json/jsServices/VoiceTraSS'

# read the locations, objects and sentences files
# and clean up the lists from the files
rooms           = []
locations       = []
items           = []
class_items     = []
cat1Sentences   = []
cat2Sentences   = []
cat3Situations  = []
names           = []
# get rid of empty lines and do not use anything that starts with a '#'
# '#'はコメントアウトの飛ばす.
for room in [line.strip('\n') for line in open('rooms.txt', 'r').readlines()]:
    if room != '': #データないなら飛ばす
        if room[0] != '#':
            rooms.append(room)
for loc in [location.strip('\n') for location in open('locations.txt', 'r').readlines()]:
    if loc != '':
        if loc[0] != '#':
            locations.append(loc)
for it  in [item.strip('\n')     for item     in open('items.txt',   'r').readlines()]: #改行で配列に入れる
    if it  != '':
        if it[0] != '#':
            items.append(it)
for ci  in [class_item.strip('\n')     for class_item     in open('class_items.txt',   'r').readlines()]:
    if ci  != '':
        if ci[0] != '#':
            class_items.append(ci)
#ここまで品物類です．

for sentence in [str(sent).strip('\n') for sent in open('cat1Sentences.txt' , 'r').readlines()]:
    if sentence != '':
        if sentence[0] != '#':
            cat1Sentences.append(sentence)
for sentence in [str(sent).strip('\n') for sent in open('cat2Sentences.txt' , 'r').readlines()]:
    if sentence != '':
        if sentence[0] != '#':
            cat2Sentences.append(sentence)

situations  = []
questions   = []
for sit in [str(sent).strip('\n') for sent in open('cat3Situations.txt' , 'r').readlines()]:
    if sit != '':
        if sit[0] != '#':
            if sit.split()[0] == 'situation:':
                situations.append( sit )
            if sit.split()[0] == 'question:':
                questions.append( sit )
cat3Situations = zip( situations, questions )

for name in [nam.strip('\n')     for nam     in open('names.txt',   'r').readlines()]:
    if name  != '':
        if name[0] != '#':
            names.append(name)

# are there at least two locations?
if len(locations) < 2: #ロケーションが２つ以上ないとダメ
    print 'Not enough locations. Exiting program'
    sys.exit(1)
# are there at least two items?
if len(items) < 2: #アイテムが２つ以上ないとダメ
    print 'Not enough items. Exiting program'
    sys.exit(1)
#-----------------------------------ここまでデータ宣言している．----------------------------------#

# the function 'fillIn' takes a sentence and replaces
# the word 'location' for an actual location
# and replaces the word 'item' for an actual item
# as defined in the files:
# locations.txt
# and items.txt
#random.shuffle(

def fillIn(sentence):
    #shuffle the items and the locations
    random.shuffle(rooms)#リストをランダムソート
    random.shuffle(items)
    random.shuffle(class_items)
    random.shuffle(locations)
    random.shuffle(names)
    #fill in the locations and items in the sentence
    # the counters are used so an item or location is not used twice
    # hence the shuffeling for randomization
    roomCounter         = 0
    itemCounter         = 0
    class_itemCounter   = 0
    locationCounter     = 0
    nameCounter         = 0
    finalSentence       = []

    #センテンスとラベルどっちにも加える；

    for word in sentence.split(' '):#センテンスを
#	print word
        # fill in a room
        #
        if word == 'ROOM':
            finalSentence.append( rooms[roomCounter] )
            roomCounter += 1
        # or fill in a location
        elif word == 'LOCATION':
            finalSentence.append( locations[locationCounter] )
            locationCounter += 1
        # or an item
        elif word == 'ITEM':
            finalSentence.append( items[itemCounter] )
            itemCounter += 1
        # or an item class
        elif word == 'CLASS_ITEM':
            finalSentence.append( class_items[class_itemCounter] )
            class_itemCounter += 1
        # is it a name?
        elif word == 'NAME':
            finalSentence.append( names[nameCounter] )
            nameCounter += 1
        # perhaps a location with a comma or dot?
        elif word[:-1] == 'LOCATION':
            finalSentence.append( locations[locationCounter] + word[-1])
            locationCounter += 1
        # or an item with a comma or dot or whatever
        elif word[:-1] == 'ITEM':
            finalSentence.append( items[itemCounter] + word[-1])
            itemCounter += 1
        # is it a namewith a comma, dot, whatever?
        elif word[:-1] == 'NAME':
            finalSentence.append( names[nameCounter] + word[-1] )
            nameCounter += 1
        # or else just the word
        else:
            finalSentence.append( word )
    # then make a sentence again out of the created list
#	    print finalSentence
    out = ' '.join(finalSentence)
    #print(out)
    out = out.replace('    ', '  ')
    out = out.replace('   ', '  ')
    # out = out.replace('  ', ' ')
    # return ' '.join(finalSentence)
    return out


# the tests are defined here
#cat1Sentences で

def testOne():
    df = pd.DataFrame([],columns=["SentenceGPSR"])
    #100sentence
    #for i in range(100):
    sentence = pd.DataFrame([fillIn(random.choice(cat1Sentences) )],columns=["SentenceGPSR"])
    df = df.append(sentence)
    #yotaコメントアウト
    print('\n%s\n\n' % sentence)
    #df.drop_duplicates(["SentenceGPSR"])
    #df.to_csv("GPSRSentenceJP.csv",index=False,mode='a',header=False,encoding="cp932")

    # say(sentence)

# Category 2
def testTwo():
    sentence = fillIn( random.choice(cat2Sentences) )
    print('\n%s\n\n' % sentence)
    # say(sentence)

# Category 3
def testThree():
    print 'This is the situation for category 3, press enter for the question.\n\n'
    situation = random.choice( cat3Situations )
    print fillIn(situation[0].split(':')[1])
    # print situation[0].split(':')[1]
    # raw_input()
    sentence = fillIn(situation[1].split(':')[1])
    print('%s\n\n' % sentence)
    # print '\n\n'
    # say(sentence)

#############################################  MAIN LOOP ####################################
def say(sentence):
    # command
    tts_command = { "method":"speak", "params":["1.1",  {"language":"ja","text":sentence,"voiceType":"*","audioType":"audio/x-wav"}]}

    obj_command = json.dumps(tts_command)     # string to json object
    req = urllib2.Request(tts_url, obj_command)
    received = urllib2.urlopen(req).read()    # get data from server

    # extract wav file
    obj_received = json.loads(received)
    tmp = obj_received['result']['audio'] # extract result->audio
    speech = base64.decodestring(tmp.encode('utf-8'))

    f = open ("out.wav",'wb')
    f.write(speech)
    f.close
    os.system("aplay out.wav")

#DOING yota

# ask the user which test this program should generate
def mainLoop():
    answer = 'begin'
        #while True:
    while range(10000):
        answer = raw_input('Which category do you want to do?\nPossible answers are: 1, 2, 3 or q(uit)')
        #answer = '1'
        if answer == 'q':
            print 'Exiting program.'
            sys.exit(1)
        elif answer == '1':
            print 'Category 1:\n',
            testOne()
        elif answer == '2':
            print 'Category 2:\n'
            testTwo()
        elif answer == '3':
            print 'Category 3:\n'
            testThree()
        else:
            print '\nNot a valid input, please try 1, 2, 3 or q(uit)\n'

if __name__ == "__main__":
    mainLoop()
