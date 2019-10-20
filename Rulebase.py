def remove(line):
    line = line.replace('would','')
    line = line.replace('you','')
    line = line.replace('can','')
    line = line.replace('well','')
    line = line.replace('er','')
    line = line.replace('please','')
    line = line.replace('and','')
    line = line.replace('next','')
    line = line.replace('then','')
    line = line.replace('finally','')
    line = line.replace('okay','')
    return line

def create_command(line):
    command = ""
    while True:
        if(line[0] == 'go' or line[0] == 'move'):
            command = command + ' Move ( '
            if 'go' in line[1:]:
                if line[3:].index('go') == 0:
                    command = command + line[2] + ' ) '
                    del line[0:3]
                elif line[3:].index('go') == 0:
                    command = command + line[2] + '_' + line[3] + ' ) '
                    del line[0:4]
            elif 'move' in line[1:]:
                if line[3:].index('move') == 0:
                    command = command + line[2] + ' ) '
                    del line[0:3]
                elif line[4:].index('move') == 0:
                    command = command + line[2] + '_' + line[3] + ' ) '
                    del line[0:4]
            elif  'take' in line:
                if line.index('take') == 3:
                    command = command + line[2] + ' ) ' + ' Find '
                    del line[0:3]
                elif line.index('take') == 4:
                    command = command + line[2] + '_' +line[3] + ' ) '
                    del line[0:4]
            elif 'detect' in line:
                if line.index('detect') == 3:
                    command = command + line[2] + ' ) '
                    command = command + ' Find ( ' + line[4] + ' ) '
                    del line[0:4]
                elif line.index('detect') == 4:
                    command = command + line[2] + '_' +line[3] + ' ) '
                    command = command + ' Find ( ' + line[5] + ' ) '
                    del line[0:5]
            elif 'get' in line:
                if line.index('get') == 3:
                    command = command + line[2] + ' ) '
                    command = command + ' Find ( ' + line[4] + ' ) '
                    del line[0:4]
                elif line.index('get') == 4:
                    command = command + line[2] + '_' +line[3] + ' ) '
                    command = command + ' Find ( ' + line[5] + ' ) '
                    del line[0:5]
            elif 'find' in line:
                if line.index('find') == 3:
                    command = command + line[2] + ' ) '
                    command = command + ' Find ( ' + line[4] + ' ) '
                    del line[0:4]
                elif line.index('find') == 4:
                    command = command + line[2] + '_' +line[3] + ' ) '
                    command = command + ' Find ( ' + line[5] + ' ) '
                    del line[0:5]
            elif 'grasp' in line:
                if line.index('grasp') == 3:
                    command = command + line[2] + ' ) '
                    command = command + ' Find ( ' + line[4] + ' ) '
                    del line[0:4]
                elif line.index('grasp') == 4:
                    command = command + line[2] + '_' +line[3] + ' ) '
                    command = command + ' Find ( ' + line[5] + ' ) '
                    del line[0:5]
            elif 'come' in line[1:]:
                if line.index('come') == 3:
                    command = command + line[2] + ' ) '
                    command = command + ' Find ( ' + line[4] + ' ) '
                    del line[0:4]
                elif line.index('come') == 4:
                    command = command + line[2] + '_' +line[3] + ' ) '
                    command = command + ' Find ( ' + line[5] + ' ) '
                    del line[0:5]               
            '''
            
            elif(line[3] == 'find'):
                command = command + ' Find '
            elif(line[4] == 'grasp'):
                command = command + ' Find '
            elif(line[0] == 'bring' or line[0] == 'get'):
                command = command + ' Move ( '
            '''
        
        elif((line[0] == 'leave' or line[0] == 'exit') and line[1] == 'the' and line[2] == 'apartment'):
            command = command + ' Move ( apartment ) '
        elif(line[0] == 'come' and line[1] == 'back'):
            command = command + ' Move ( HERE ) '
        elif(line[0] == 'exit'):
            command = command + ' Move ( ' + line[2] + ')'
        elif(line[0] == 'call'):
            command = command + ' Say ( person ) '
        
        line.pop(0)
        if len(line)==0:
            break;
    return command

if __name__ == '__main__':
    file = "./speech_recognition_results/speaker_W/google_wordresultdata.csv"
    f = open(file,mode='r')
    line = f.readline()
    while line:
        line = remove(line)
        line = line.split()
        print(line)
        print(create_command(line))
        line = f.readline()
    f.close()
