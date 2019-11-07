import random
import pandas as pd

def remove(line):
    line = line.replace('would','')
    line = line.replace('you','')
    line = line.replace('can ',' ')
    line = line.replace('well','')
    line = line.replace(' er',' ')
    line = line.replace('please','')
    line = line.replace('and','')
    line = line.replace('next ','')
    line = line.replace('then ','')
    line = line.replace('finally','')
    line = line.replace('okay','')
    return line

verbs = ['go','move','take','get','detect','find','grasp','bring','leave','come','exit','call','carry','place','put','throw','ask','follow']

def conbine_words(words):
    try:
        conbined_words = str(words[0])
        for word in words[1:]:
            conbined_words = conbined_words + '_' +str(word)
        return conbined_words
    except:
        return None

def check_command_items(non_verb):
    try:
        for item in items:
            if len(non_verb) == 4:
                if non_verb[0] + ' ' +non_verb[1] + ' ' + non_verb[2] + ' ' + non_verb[3]  == str.lower(item):
                    return item.replace(' ','_')
            if len(non_verb) == 3:
                if non_verb[0] + ' ' +non_verb[1] + ' ' + non_verb[2] == str.lower(item):
                    return item.replace(' ','_')               
            if non_verb[0] == str.lower(item):
                return item
            if len(non_verb) > 1:
                if non_verb[1] == str.lower(item):
                    return item
                elif non_verb[0] + ' ' +non_verb[1] == str.lower(item):
                    return item.replace(' ','_')
                
        return random.choice(items).replace(' ','_')
    except:
        return random.choice(items).replace(' ','_')
        
    
def check_command_places(non_verb):
    try:
        if len(non_verb)==1 and non_verb[0]=='kitchen':
            return 'kitchen'
        elif non_verb[0]=='kitchen' and non_verb[1]=='table':
            return 'Kitchen_Table'
        elif non_verb[0]=='kitchen' and non_verb[1]=='room':
            return 'Kitchen_Room'
        for room in rooms:
            if non_verb[0] == str.lower(room):
                return room
            if len(non_verb) > 1:
                if non_verb[0] + ' ' + non_verb[1] == str.lower(room):
                    return room.replace(' ','_')
        for location in locations:
            if non_verb[0] == str.lower(location):
                return location
            if len(non_verb) > 1:
                if non_verb[0] + ' ' + non_verb[1] == str.lower(location):
                    return location.replace(' ','_')
        return random.choice(rooms).replace(' ','_')
    except:
        return random.choice(rooms).replace(' ','_')

def create_command(line):
    command = ""
    sentence_verb = []
    sentence_non_verb = []
    non_verb = []
    command_verb = []
    command_objective = []
    for i,word in enumerate(line):
        if word in verbs:
            if len(sentence_verb)!=0:
                sentence_non_verb.append(non_verb)
                non_verb = []
            sentence_verb.append(word)
        elif len(sentence_verb)!=0:
            non_verb.append(word)
    sentence_non_verb.append(non_verb)
    #print(sentence_verb)
    #print(sentence_non_verb)
    #print("\n")
    while len(sentence_verb)!=0:
        verb = sentence_verb.pop(0)
        if verb in ('go','move'):
            command_verb.append('Move')
            place = check_command_places(sentence_non_verb.pop(0)[1:])
            command_objective.append(place)
            try:
                if sentence_verb[0] in ('take','get','detect','find','grasp'):
                    verb = sentence_verb.pop(0)
                    if verb == 'take':
                        if sentence_verb == []:
                            item = check_command_items(sentence_non_verb.pop(0))
                            command_verb.append('Find')
                            command_objective.append((item,place))
                            command_verb.append('Grasp')
                            command_objective.append(item)
                            command_verb.append('Move')
                            command_objective.append('HERE')
                        elif sentence_verb[0] in ('bring','carry','place','come','put','leave'):
                            verb = sentence_verb.pop(0)
                            item = check_command_items(sentence_non_verb.pop(0))
                            if verb == 'bring':
                                place2 = check_command_places(sentence_non_verb.pop(0)[2:])                                
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append(place2)
                                # on:96
                                #command_objective.append(place)
                            elif verb in ('carry','place'):
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append(place)
                            elif verb == 'come':
                                # on:55,98
                                #command_verb.append('Find')
                                #command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append('HERE')
                            elif verb == 'put':
                                place2 = check_command_places(sentence_non_verb.pop(0)[2:])
                                # on:9,26,41,90
                                #command_verb.append('Find')
                                #command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append(place2)
                                command_verb.append('Place')
                                # on:3
                                #command_objective.append(item)
                                command_objective.append((item,place))
                                #command_objective.append((item,place2))
                            elif verb == 'leave':
                                place2 = check_command_places(sentence_non_verb.pop(0)[1:])
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append(place2)
                    elif verb == 'get':
                        if sentence_verb == []:
                            item = check_command_items(sentence_non_verb.pop(0))
                            command_verb.append('Find')
                            command_objective.append((item,location))
                            command_verb.append('Grasp')
                            command_objective.append(item)
                        elif sentence_verb[0] in ('come','exit','place','throw','carry','bring'):
                            verb = sentence_verb.pop(0)
                            item = check_command_items(sentence_non_verb.pop(0))
                            if verb == 'come':
                                # on:30,35,37
                                #command_verb.append('Find')
                                #command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                # 59:on
                                #command_verb.append('Move')
                                #command_objective.append(place)
                                #command_verb.append('Grasp')
                                #command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append('HERE')
                            elif verb == 'exit':
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                room = check_command_places(sentence_non_verb.pop(0)[1:])
                                command_objective.append(room)
                            elif verb == 'place':
                                '''
                                # on:88
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                place2 = check_command_places(sentence_non_verb.pop(0)[2:])
                                command_verb.append('Move')
                                command_objective.append(place2)
                                command_verb.append('Place')
                                command_objective.append((item,place))
                                '''
                                # off:6 
                                #command_verb.append('Find')
                                #command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                place2 = check_command_places(sentence_non_verb.pop(0)[2:])
                                command_verb.append('Move')
                                command_objective.append(place2)
                                command_verb.append('Place')
                                # off:6
                                #command_objective.append((item,place))
                                # on:6
                                command_objective.append(item)
                            elif verb == 'throw':
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append('Dustbin')
                                command_verb.append('Place')
                                command_objective.append((item,'Dustbin'))
                            elif verb == 'carry':
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                #place2=check_command_places(sentence_non_verb.pop(0))
                                command_verb.append('Move')
                                command_objective.append(place)
                            elif verb == 'bring':
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                #place2=check_command_places(sentence_non_verb.pop(0))
                                command_verb.append('Move')
                                command_objective.append(place)
                    elif verb == 'detect':
                        item = check_command_items(sentence_non_verb.pop(0))
                        if sentence_verb == []:
                            command_verb.append('Find')
                            command_objective.append((item,place))
                        elif sentence_verb[0] in ('take','get','grasp'):
                            command_verb.append('Find')
                            command_objective.append((item,place))
                            command_verb.append('Grasp')                       
                            command_objective.append(item)
                    elif verb == 'find':
                        if sentence_verb == []:
                            command_verb.append('Find')
                            item = check_command_items(sentence_non_verb.pop(0))
                            command_objective.append((item,place))
                        elif sentence_verb[0] in ('bring','get','follow','grasp','take'):
                            verb = sentence_verb.pop(0)
                            non_verb = sentence_non_verb.pop(0)
                            if verb == 'bring':
                                if 'person' in non_verb:
                                    command_verb.append('Find')
                                    command_objective.append(('person',place))
                                    item_and_place = sentence_non_verb.pop(0)
                                    if 'from' in item_and_place:
                                        fr = item_and_place.index('from')
                                        item = check_command_items(item_and_place[:fr])
                                        place = check_command_places(item_and_place[fr+1:])
                                        command_verb.append('Move')
                                        command_objective.append(place)
                                        command_verb.append('Grasp')
                                        command_objective.append(item)
                            elif verb == 'get':
                                command_verb.append('Move')
                                command_objective.append(check_command_places(sentence_non_verb.pop(0)))
                                command_verb.append('Grasp')
                            elif verb == 'follow':
                                command_verb.append('Find')
                                command_objective.append(('person',place))
                                command_verb.append('Follow')
                                command_objective.append('person')
                            elif verb == 'grasp':
                                item = check_command_items(non_verb)
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                            elif verb == 'take':
                                item = check_command_items(non_verb)
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                    elif verb == 'grasp':
                        item = check_command_items(sentence_non_verb.pop(0))
                        if sentence_verb == []:
                            command_verb.append('Grasp')
                            command_objective.append(item)
                        elif sentence_verb[0] in ('bring','throw','place','come'):
                            verb =sentence_verb.pop(0)
                            if verb == 'bring':
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                place2 = check_command_places(sentence_non_verb.pop(0)[2:])
                                command_verb.append('Move')
                                command_objective.append(place2)
                                command_verb.append('Find')
                                command_objective.append((item,place2))
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append(place)
                            elif verb == 'throw':
                                print(item)
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append('Dustbin')
                                command_verb.append('Place')
                                command_objective.append((item,'Dustbin'))
                            elif verb == 'place':
                                command_verb.append('Grasp')
                                command_verb.append('Move')
                                command_verb.append('Place')
                            elif verb == 'come':
                                # off:31,33,53,83
                                command_verb.append('Find')
                                command_objective.append((item,place))
                                # off:39,94
                                command_verb.append('Grasp')
                                command_objective.append(item)
                                command_verb.append('Move')
                                command_objective.append('HERE')
                        else:
                            # off:2 on:64,72
                            #command_verb.append('Find')
                            #command_objective.append((item,place))
                            command_verb.append('Grasp')
                            command_objective.append(item)
            except:
                continue
        elif verb == 'get':
            # TODO:38
            item_and_place = sentence_non_verb.pop(0)
            if 'from' in item_and_place:
                fr = item_and_place.index('from')
                item = check_command_items(item_and_place[:fr])
                place = check_command_places(item_and_place[fr+1:])
                command_verb.append('Move')
                command_objective.append(place)
                # on:38
                #command_verb.append('Find')
                #command_objective.append((item,place))            
                command_verb.append('Grasp')
                command_objective.append(item)
        elif verb == 'bring':
            item_and_place = sentence_non_verb.pop(0)
            if 'from' in item_and_place:
                fr = item_and_place.index('from')
                item = check_command_items(item_and_place[:fr])
                place = check_command_places(item_and_place[fr+1:])
                command_verb.append('Move')
                command_objective.append(place)
                #command_verb.append('Find')
                #command_objective.append('dummy')            
                command_verb.append('Grasp')
                command_objective.append(item)
        elif verb == 'leave':
            command_verb.append('Move')
            command_objective.append('apartment')
        elif verb == 'exit':
            command_verb.append('Move')
            place = check_command_places(sentence_non_verb.pop(0)[1:])
            command_objective.append(place)
        elif verb == 'come':
            command_verb.append('Move')
            command_objective.append('HERE')
        elif verb == 'call':
            command_verb.append('Say')
            command_objective.append('person')
            try:
                item_and_place = sentence_non_verb.pop(2)       
                fr = item_and_place.index('from')
                item = check_command_items(item_and_place[:fr])
                place = check_command_places(item_and_place[fr+1:])
            except:
                item = 'dummy'
                place = 'dummy'
            command_verb.append('Listen')
            command_objective.append(item)
            command_verb.append('Move')
            command_objective.append(place)
            command_verb.append('Find')
            # on:12 off:70
            #command_objective.append(item)
            # on:70 off:12
            command_objective.append((item,place))
            command_verb.append('Grasp')
            command_objective.append(item)
            command_verb.append('Move')
            command_objective.append(item)
            command_verb.append('Place')
            # on:12 off:70
            #command_objective.append(item)
            # on:70 off:12
            command_objective.append((item,place))
    #print(command_verb)
    #print(command_objective)
    command = assemble_command(command_verb,command_objective)
    return command

def assemble_command(command_verb,command_objective):
    assembled_command = ''
    for (verb,objective) in zip(command_verb,command_objective):
        if len(objective) == 2:
            assembled_command = assembled_command + verb + ' ( ' + objective[0] + ' ' + objective[1] + ' ) '
        else:
            assembled_command = assembled_command + verb + ' ( ' + objective + ' ) '
    return assembled_command
    
items = []
locations = []
rooms = []

if __name__ == '__main__':
    
    file = "./speech_recognition_results/speaker_W/sphinx_wordresultdata.csv"
    f = open(file,mode='r')
    
    file_items = "./GPSRDATA/items.txt"
    fi = open(file_items,mode='r')
    for item in [line.strip('\n') for line in fi.readlines()]:
        if item != '':
            if item[0] != '#':
                items.append(item)

    #print(items)
    #print('####')

    file_locations = "./GPSRDATA/locations.txt"
    fl = open(file_locations,mode='r')
    for location in [line.strip('\n') for line in fl.readlines()]:
        if location != '':
            if location[0] != '#':
                locations.append(location)
    #print(locations)
    #print('####')

    file_rooms = "./GPSRDATA/rooms.txt"
    fr = open(file_rooms,mode='r')
    for room in [line.strip('\n') for line in fr.readlines()]:
        if room != '':
            if room[0] != '#':
                rooms.append(room)
    rooms.append('apartment')
    #print(rooms)    
    #print('####')
    '''
    sum = 0
    correct =[]
    df=pd.read_csv("GPSRsentence_list.csv")
    for i in range(100):
        print(i)
        line = df.loc[i,'original_sentence']
        print(line)   
        line = remove(line)
        line = line.replace('.','')
        line = str.lower(line)
        line = line.replace('_',' ')
        #print(line)
        line = line.split()
        created_command = create_command(line)
        print('created_command : ' + created_command)
        label = df.loc[i,'label']
        label = label.replace('  ',' ')
        label = label + ' '
        print('label           : ' + label)
        if created_command == label:
            print("OK")
            sum = sum + 1
            correct.append(i)
        print('\n')
    print(sum)
    print(correct)
    print([3,7,9,12,15,17,24,25,26,30,31,33,35,37,38,39,41,53,55,59,64,72,74,83,88,90,94,96,98])
    '''
    df=pd.read_csv("GPSRsentence_list.csv")
    lines = f.readlines()
    for i in range(100):
        #print(i)
        #print(df.loc[i,'original_sentence'])       
        line = lines[i]
        #print(line)
        line = remove(line)
        line = line.split()
        print(create_command(line))
        #print(df.loc[i,'label'])
        #print('\n')
        line = f.readline()

    f.close()

