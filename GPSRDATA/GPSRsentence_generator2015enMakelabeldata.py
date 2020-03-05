import random
import sys
import pandas as pd
from tqdm import tqdm

rooms = []
locations = []
items = []
cat1Sentences = []

for room in [line.strip("\n") for line in open("rooms.txt", "r").readlines()]:
    if room != "":
        if room[0] != "#":
            room = room.replace(" ", "_")
            rooms.append(room)

for location in [line.strip("\n") for line in open("locations.txt", "r").readlines()]:
    if location != "":
        if location[0] != "#":
            location = location.replace(" ", "_")
            locations.append(location)

for item in [line.strip("\n") for line in open("items.txt", "r").readlines()]:
    if item != "":
        if item[0] != "#":
            item = item.replace(" ", "_")
            items.append(item)

filename = "cat1Sentences.en.xlsx"
df = pd.read_excel(filename, sheet_name="Sheet1")
for sentence in df["Sentence"]:
    if sentence != "":
        if sentence[0] != "#":
            cat1Sentences.append(sentence)

labeldatas = []
labelSetdatas = []

for label in df["label"]:
    if label != "":
        labeldatas.append(label)

for i in range(len(cat1Sentences)):
    labelSetdatas.append([cat1Sentences[i], labeldatas[i]])

if len(locations) < 2:
    print("Not enough locations. Exiting program")
    sys.exit(1)

if len(items) < 2:
    print("Not enough items. Exiting program")
    sys.exit(1)

# the function 'fillIn' takes a sentence and replaces
# the word 'location' for an actual location
# and replaces the word 'item' for an actual item


def fillIn(labelSetdatas):
    sentences = labelSetdatas[0]

    labels = labelSetdatas[1]
    random.shuffle(rooms)
    random.shuffle(items)
    random.shuffle(locations)
    # fill in the locations and items in the sentence
    # the counters are used so an item or location is not used twice
    # hence the shuffeling for randomization
    roomCounter = 0
    itemCounter = 0
    locationCounter = 0
    finalSentence = []

    roomLabel = []
    itemLabel = []
    locationLabel = []
    finalLabel = []

    for word in sentences.split(" "):
        if word == "ROOM":
            finalSentence.append(rooms[roomCounter])
            roomLabel.append(rooms[roomCounter])
            roomCounter += 1
        elif word == "LOCATION":
            finalSentence.append(locations[locationCounter])
            locationLabel.append(locations[locationCounter])
            locationCounter += 1
        elif word == "ITEM":
            finalSentence.append(items[itemCounter])
            itemLabel.append(items[itemCounter])
            itemCounter += 1
        # perhaps a location with a comma or dot?
        elif word[:-1] == "LOCATION":
            # print(word[:-1])
            finalSentence.append(locations[locationCounter] + word[-1])
            locationLabel.append(locations[locationCounter] + word[-1])
            locationCounter += 1
        # or an item with a comma or dot or whatever
        elif word[:-1] == "ITEM":
            finalSentence.append(items[itemCounter] + word[-1])
            itemLabel.append(items[itemCounter] + word[-1])
            itemCounter += 1
        # or else just the word
        else:
            finalSentence.append(word)

    if roomCounter > 3 or itemCounter > 3 or locationCounter > 3:
        print("--------------------end------------------------")

    roomLabelCounter = 0
    itemLabelCounter = 0
    locationLabelCounter = 0

    if str(labels) != "nan":
        for label in labels.split(" "):
            if label.find(u",") > -1:
                continue
            if label.find(u"Find") > -1 or label.find(u"Place") > -1:
                if roomLabelCounter >= 1:
                    roomLabelCounter -= 1
                elif locationLabelCounter >= 1:
                    locationLabelCounter -= 1
            if label.find(u"ROOM") > -1:
                label = label.replace(u"ROOM", roomLabel[roomLabelCounter])
                if roomCounter >= 2 and roomLabelCounter < 1:
                    roomLabelCounter += 1
            elif label.find(u"LOCATION") > -1:
                label = label.replace(u"LOCATION", locationLabel[locationLabelCounter])
                if locationCounter >= 2 and locationLabelCounter < 1:
                    locationLabelCounter += 1
            elif label.find(u"ITEM") > -1:
                label = label.replace("ITEM", itemLabel[itemLabelCounter])
                if itemCounter >= 2 and itemLabelCounter < 1:
                    itemLabelCounter += 1
            finalLabel.append(label)
        outfinalLabel = " ".join(finalLabel)
        outfinalLabel = outfinalLabel.replace('"[', "")
        outfinalLabel = outfinalLabel.replace(']"', "")
    else:
        outfinalLabel = "NULL"
    # then make a sentence again out of the created list
    out = " ".join(finalSentence)
    out = out.replace("    ", " ")
    out = out.replace("   ", " ")
    out = out.replace("  ", " ")
    outfinalLabel = "".join(outfinalLabel)
    outfinalLabel = outfinalLabel.replace("    ", " ")
    outfinalLabel = outfinalLabel.replace("   ", " ")
    outfinalLabel = outfinalLabel.replace("  ", " ")

    # print(outfinalLabel)
    return out, outfinalLabel


if __name__ == "__main__":
    df = pd.DataFrame([], columns=["data", "labeldata"])
    for i in tqdm(range(15000)):
        random.shuffle(labelSetdatas)
        sentence = pd.DataFrame(
            [fillIn(labelSetdatas[0])], columns=["data", "labeldata"]
        )
        df = df.append(sentence)
    df.drop_duplicates(["data"])
    df.to_csv(
        "tempGPSRSentence.csv", index=False, mode="w", header=False, encoding="cp932"
    )
