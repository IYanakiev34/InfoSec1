import sys


def firstLine():
    input_list = input().split(' ')
    
    if len(input_list) % 2 == 1:
        input_list.pop(len(input_list) - 1)

    actions = []
    values = []

    for index,item in enumerate(input_list):
        if index % 2 == 0:
            # Action
            actions.append(item)
        else:
            values.append(item)


    result_list = list(zip(actions,values))

    return result_list

def generateShift(action,value,shift = []):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    curr_shift = [None]*26
    for index,i in enumerate(shift):
        curr_shift[index] = i


    # If the value is a mapping
    if value.isalpha() and len(value) == 26:
        if action == 'e':
            for index,i in enumerate(value):
                # shift[index] = get index of the shift element in th alphabet and then see its mapping
                shift[index] = value[alph.index(shift[index])]
        elif action == 'd':
            for index,i in enumerate(value):
                shift[index] = alph[value.index(shift[index])]
        return shift
    # Value is not mapping
    value = abs(int(value)) % 26
    
    if value == 0:
        return shift


    if action == 'e':
        for i in range(0,26):
            shift[i] = chr(ord('a') +  (ord(curr_shift[i]) - ord('a') + value) % 26)
    elif action == 'd':
        for i in range(0,26):
            shift[i] = chr(ord('a') + (ord(curr_shift[i]) - ord('a') + (26 - value)) % 26)

    return shift


def applyShift(shift,line):
    new_line = [None]*len(line)
    
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for index,i in enumerate(line):
        if i.isalpha():
            if i.islower():
                new_line[index] = shift[alph.index(i)]            
            else:
                new_line[index] = shift[alph.index(i.lower())].upper()
        else:
            new_line[index] = i

    return new_line    

if __name__ == "__main__":
    # Gathering the action list needed
    result_list = firstLine()
   
    shift = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for (i,j) in result_list:
        shift = generateShift(i,j,shift)

    for line in sys.stdin:
        line = applyShift(shift,line)
        print(''.join(line).replace('\n',''))






