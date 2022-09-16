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

# Shifting the normal lphabet by some value
def generateShift(action,value):
     
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # 0 or 26 == no shift
    if value == 0 or value == 26:
        return alph
    
    shift = [None]*26

    # if we have a mapping convert shhift to mapping 
    if value.isalpha() and len(value) == 26:
        value = list(value)
        for index,i in enumerate(value):
            shift[index] = i
        return shift

    # create shift 
    if action == 'e':
        #Get the value since it can be negative make abs and mod 26 also
        value = abs(int(value)) % 26
        
        # standard shifting for encryption
        for i in range(0,26):
            shift[i] = alph[(i + value) % 26]
    
    elif action == 'd':
        # Get value and perform again encryption but with 26 - value
        value = 26 - abs(int(value)) % 26
        
        # Same thing as encryption
        for i in range(0,26):
            shift[i] =alph[(i + value) % 26]
    
    # return the shift
    return shift

def applyShiftToLine(line,shift):
    new_line = [None]*len(line)

    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # Take line[i] and i
    for index,i in enumerate(line):
        # if character perform encryption or ecryption else just add it
        if i.isalpha():

            # if is lower just encrypt/decrypt
            if i.islower():
                new_line[index] = shift[alph.index(i)]            
            # else we need to convert back to upper
            else:
                new_line[index] = shift[alph.index(i.lower())].upper()
        # if not alphabetic just add it
        else:
            new_line[index] = i    
            
    return new_line

if __name__ == "__main__":
    # Gathering the action list needed
    result_list = firstLine()
   
    # The shift list which will contain all the operations we need to perform on a line of text in order
    shift_list = []
    
    # shift list generation (i,j) => i == action, j == value e.g('e',5)
    for (i,j) in result_list:
        shift_list.append(generateShift(i,j))
    
    input_lines = []
    
    for line in sys.stdin:
        input_lines.append(line)
        
    result_list = []    
    for line in input_lines:
        for i in shift_list:
            line = applyShiftToLine(line,i)

        line = ''.join(line).replace('\n','')
        result_list.append(line)

    for i in result_list:
        print(i)
