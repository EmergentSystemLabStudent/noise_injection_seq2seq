import random
import sys
import copy
import os
import pandas as pd
import string
import base64
import json
import wave
import math

# read the locations, objects and sentences files
# and clean up the lists from the files
rooms           = []
locations       = []
items           = []
#class_items     = []
cat1Sentences   = []
#cat2Sentences   = []
#cat3Situations  = []
#names           = []

# get rid of empty lines and do not use anything that starts with a '#'
for room in [line.strip('\n') for line in open('rooms.txt', 'r').readlines()]:
    if room != '':
        if room[0] != '#':
            room = room.replace(' ', '_')
            rooms.append(room)

for location in [line.strip('\n') for line in open('locations.txt', 'r').readlines()]:
    if location != '':
        if location[0] != '#':
            location = location.replace(' ', '_')
            locations.append(location)

for item  in [line.strip('\n')     for line     in open('items.txt',   'r').readlines()]:
    if item  != '':
        if item[0] != '#':
            item = item.replace(' ', '_')
            items.append(item)

#for ci  in [class_item.strip('\n')     for class_item     in open('class_items.txt',   'r').readlines()]:
#    if ci  != '':
#        if ci[0] != '#':
#            ci = ci.replace(' ', '_')
#            class_items.append(ci)

filename = "cat1Sentences.en.xlsx"
df = pd.read_excel(filename, sheet_name='Sheet1')
for sentence in df['Sentence']:
    if sentence != '':
        if sentence[0] != '#':
            cat1Sentences.append(sentence)

labeldatas =[]
labelSetdatas = []
ndata = len(cat1Sentences)

for label in df['label']:
    if label != '':
            labeldatas.append(label)

for i in range(ndata):
    labelSetdatas.append([cat1Sentences[i],labeldatas[i]])


#for sentence in [str(sent).strip('\n') for sent in open('cat2Sentences.txt' , 'r').readlines()]:
#    if sentence != '':
#        if sentence[0] != '#':
#            cat2Sentences.append(sentence)

#situations  = []
#questions   = []
#for sit in [str(sent).strip('\n') for sent in open('cat3Situations.txt' , 'r').readlines()]:
#    if sit != '':
#        if sit[0] != '#':
#            if sit.split()[0] == 'situation:':
#                situations.append( sit )
#            if sit.split()[0] == 'question:':
#                questions.append( sit )
#cat3Situations = zip( situations, questions )

#for name in [nam.strip('\n')     for nam     in open('names.txt',   'r').readlines()]:
#    if name  != '':
#        if name[0] != '#':
#            names.append(name)

# are there at least two locations?
if len(locations) < 2:
    print ('Not enough locations. Exiting program')
    sys.exit(1)
# are there at least two items?
if len(items) < 2:
    print ('Not enough items. Exiting program')
    sys.exit(1)

# the function 'fillIn' takes a sentence and replaces
# the word 'location' for an actual location
# and replaces the word 'item' for an actual item
# as defined in the files:
# locations.txt
# and items.txt
# random.shuffle(

def fillIn(labelSetdatas):
    sentences = labelSetdatas[0]

    labels = labelSetdatas[1]
    # shuffle the items and the locations
    random.shuffle(rooms)
    random.shuffle(items)
    #random.shuffle(class_items)
    random.shuffle(locations)
    #random.shuffle(names)
    # fill in the locations and items in the sentence
    # the counters are used so an item or location is not used twice
    # hence the shuffeling for randomization
    roomCounter         = 0
    itemCounter         = 0
    #class_itemCounter   = 0
    locationCounter     = 0
    #nameCounter         = 0
    finalSentence       = []

    roomLabel = []
    itemLabel = []
    #classLabel = []
    locationLabel = []
    #nameLabel = []
    finalLabel =[]

    for word in sentences.split(' '):
        # print word
        # fill in a room
        if word == 'ROOM':
            finalSentence.append(rooms[roomCounter])
            roomLabel.append(rooms[roomCounter])
            roomCounter += 1
        # or fill in a location
        elif word == 'LOCATION':
            finalSentence.append(locations[locationCounter])
            locationLabel.append(locations[locationCounter])
            locationCounter += 1
        # or an item
        elif word == 'ITEM':
            finalSentence.append( items[itemCounter] )
            itemLabel.append(items[itemCounter])
            itemCounter += 1
        # or an item class
        #elif word == 'CLASS_ITEM':
        #    finalSentence.append( class_items[class_itemCounter] )
        #    classLabel.append(class_items[class_itemCounter])
        #    class_itemCounter += 1
        # is it a name?
        #elif word == 'NAME':
        #    finalSentence.append(names[nameCounter])
        #    nameLabel.append(names[nameCounter])
        #    nameCounter += 1
        # perhaps a location with a comma or dot?
        elif word[:-1] == 'LOCATION':
            #print(word[:-1])
            finalSentence.append(locations[locationCounter] + word[-1])
            locationLabel.append(locations[locationCounter] + word[-1])
            locationCounter += 1
        # or an item with a comma or dot or whatever
        elif word[:-1] == 'ITEM':
            finalSentence.append( items[itemCounter] + word[-1])
            itemLabel.append(items[itemCounter] + word[-1])
            itemCounter += 1
        # is it a namewith a comma, dot, whatever?
        #elif word[:-1] == 'NAME':
        #    finalSentence.append( names[nameCounter] + word[-1])
        #    nameLabel.append(names[nameCounter] + word[-1])
        #    nameCounter += 1
        # or else just the word
        else:
            finalSentence.append( word )

    #if (roomCounter  > 3 or itemCounter  > 3 or class_itemCounter > 3 or locationCounter  > 3 or nameCounter    > 3):
    if (roomCounter  > 3 or itemCounter  > 3 or locationCounter  > 3):
        print("--------------------end------------------------")

    roomLabelCounter    = 0
    itemLabelCounter    = 0
    #class_itemCounter   = 0
    locationLabelCounter     = 0
    #nameCounter         = 0

    if(str(labels) !="nan"):
        #print (labels)
        for label in labels.split(' '):
                if label.find(u',') > -1:
                    continue
                #print(label)
                if label.find(u'Find') > -1 or label.find(u'Place') > -1 :
                    if roomLabelCounter >= 1:
                        roomLabelCounter -=1
                    elif locationLabelCounter >= 1:
                        locationLabelCounter -=1
                if label.find(u'ROOM') > -1:
                    label = label.replace(u'ROOM',roomLabel[roomLabelCounter])
                    if(roomCounter >= 2 and roomLabelCounter  < 1):
                        roomLabelCounter += 1
                elif label.find(u'LOCATION') > -1:
                    label = label.replace(u'LOCATION',locationLabel[locationLabelCounter])
                    if(locationCounter >= 2 and locationLabelCounter  < 1):
                        locationLabelCounter += 1
                elif label.find(u'ITEM') > -1:
                    label = label.replace('ITEM',itemLabel[itemLabelCounter])
                    if(itemCounter >= 2 and itemLabelCounter  < 1):
                        itemLabelCounter +=1
                #elif label.find(u'CLASS_ITEM') > -1:
                #    label = label.replace('CLASS_ITEM',classLabel[class_itemCounter])
                #    class_itemCounter += 1
                #elif label.find(u'NAME') > -1:
                #    label = label.replace('NAME',nameLabel[nameCounter])
                #    nameCounter +=1
                finalLabel.append(label)
        outfinalLabel  = ' '.join(finalLabel)
        outfinalLabel = outfinalLabel.replace('\"[','')
        outfinalLabel = outfinalLabel.replace(']\"','')
    else:
        outfinalLabel = "NULL"
    # then make a sentence again out of the created list
#	    print finalSentence
    out = ' '.join(finalSentence)
    #print(out)
    out = out.replace('    ', ' ')
    out = out.replace('   ', ' ')
    out = out.replace('   ', ' ')
    outfinalLabel =''.join(outfinalLabel)
    outfinalLabel = outfinalLabel.replace('    ', ' ')
    outfinalLabel = outfinalLabel.replace('   ', ' ')
    outfinalLabel = outfinalLabel.replace('   ', ' ')

    # return ' '.join(finalSentence)
    print(outfinalLabel)
    return out,outfinalLabel

def testOne():
    df = pd.DataFrame([],columns=["data","labeldata"])
    for i in range(15000):
        random.shuffle(labelSetdatas)
        sentence = pd.DataFrame([fillIn(labelSetdatas[0])],columns=["data","labeldata"])
        df = df.append(sentence)
    df.drop_duplicates(["data"])
    df.to_csv("GPSRSentenceJP.csv",index=False,mode='a',header=True,encoding="cp932")

def mainLoop():
    print ('Category 1:\n',testOne())

if __name__ == "__main__":
    mainLoop()
