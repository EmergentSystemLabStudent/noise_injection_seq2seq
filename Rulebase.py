def remove(line):
    line = line.replace('would','')
    line = line.replace('you','')
    line = line.replace('can','')
    line = line.replace('well','')
    line = line.replace(' er',' ')
    line = line.replace('please','')
    line = line.replace('and','')
    line = line.replace('next','')
    line = line.replace('then','')
    line = line.replace('finally','')
    line = line.replace('okay','')
    return line

verbs = ['go','move','take','get','detect','find','grasp','bring','leave','come','exit','call','carry','place','put','throw']

def conbine_words(words):
    try:
        conbined_words = str(words[0])
        for word in words[1:]:
            conbined_words = conbined_words + '_' +str(word)
        return conbined_words
    except:
        return None
#def search_verb(words):
    

def create_command(line):
    command = ""
    command_verb = []
    command_objective = []
    for i,word in enumerate(line):
        for verb in verbs:
          if word == verb:
              command_verb.append((i,word))
              break
    print(command_verb)
    for i in range(len(command_verb)):
        verb = command_verb[i]
        try:
            next_verb = command_verb[i+1]
        except:
            next_verb = (len(line), None)
        command_objective.append(line[verb[0]+1:next_verb[0]])
        '''
        if(verb[1] == 'go' or verb[1] == 'move'):
            command_objective.append(line[verb[0]+2:next_verb[0]])
        elif(verb[1] in ('take','detect','get','grasp')):
            command_objective.append(line[verb[0]+1:next_verb[0]])
        elif(verb[1] in ('place','throw','bring','carry','put')):
            command_objective.append(line[verb[0]+3:next_verb[0]])
        elif(verb[1] in ('find','grasp')):
            if line[verb[0]+2] == 'person':
                command_objective.append('person')
            else:
                command_objective.append(line[verb[0]+1:next_verb[0]])
        elif(verb[1] == 'leave' or verb[1] == 'exit'):
            command_objective.append('apartment')
        elif(verb[1] == 'come'):
            command_objective.append('HERE')
        elif(verb[1] == 'call'):
            command_objective.append('person')
        '''
    print(command_objective)



    
    return command
'''
    while len(command_verb)!=0:
        if(command_verb[0][1] in ('go','move','come','leave')):
            command = command + ' Move ( ' + command_objective[0] + ' ) '
            if len(command_verb) == 1:
                command_verb.pop(0)
                command_objective.pop(0)
            elif len(command_verb) > 2:
                if command_verb[1][1] == 'take':
                    if command_verb[2][1] in ('bring','carry','place','come'):
                        command = command + 'Find ( ' + command_objective[1] + ' , ' + command_objective[0] + ' ) '
                        command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                        command = command + 'Move ( ' + command_objective[2] + ' ) '
                elif command_verb[1][1] == 'get':
                    if command_verb[2][1] == 'come':
                        command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                        command = command + 'Move ( ' + command_objective[2] + ' ) '
                    elif command_verb[2][1] == 'exit':
                        command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                        command = command + 'Move ( ' + command_objective[2] + ' ) '                  
                    elif command_verb[2][1] == 'place':
                        command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                        command = command + 'Move ( ' + command_objective[2] + ' ) '                  
                    elif command_verb[2][1] == 'throw':
                        command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                        command = command + 'Move ( ' + command_objective[2] + ' ) '                  
                elif command_verb[1][1] == 'detect':
                    command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                elif command_verb[1][1] == 'find':
                    command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                elif command_verb[1][1] == 'grasp':
                    command = command + 'Grasp ( ' + command_objective[1] + ' ) '
                del command_verb[0:2]
                del command_objective[0:2]
'''
    

if __name__ == '__main__':
    file = "./speech_recognition_results/speaker_W/google_wordresultdata.csv"
    f = open(file,mode='r')
    line = f.readline()
    while line:
        line = remove(line)
        line = line.split()
        print(line)
        print(create_command(line))
        print('\n')
        line = f.readline()
    f.close()
