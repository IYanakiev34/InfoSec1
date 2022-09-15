#!/usr/bin/python3
import sys

ORG = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def firstLine():
    input_list = input().split(' ')
    
    if len(input_list) % 2 == 1:
        input_list.pop(len(input_list) - 1)

    print(input_list)

    action_list = []
    value_list = []
    for index,item in enumerate(input_list):
        if index % 2 == 0:
            action_list.append(item)
        elif index % 2 == 1:
            value_list.append(item)
    
    result_list = list(zip(action_list,value_list))


    return result_list

def createCurrShift(encrypt,shift):
    curr_shift = [None]*26
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if len(shift) > 1 and shift.isnumeric() == False:
        for i in range(0,26):
            curr_shift[i] = shift[i]
        curr_shift.append('m')
        return curr_shift
    else:
        if encrypt == 'e':
            # Normal list
            for index,item in enumerate(alph):
                shift = int(shift)
                curr_shift[(index+shift) % 26] = item
        elif encrypt == 'd':
            alph.reverse()
            for index,item in enumerate(alph):
                shift = int(shift)
                curr_shift[(index + shift) % 26] = item
            
            curr_shift.reverse()

    curr_shift.append(encrypt)
    return curr_shift



def encryptLine(line,shift):
    new_line = []

    for i in line:
        is_alpha = i.isalpha()

        if is_alpha:
            is_low = i.islower()
            if is_low:
                # get the index of the current letter in the shift
                ind = shift.index(i)
                # alphabetic index now
                new_line.append(ORG[ind])
            else:
                ind = shift.index(i.lower())

                new_line.append(ORG[ind].upper())
        else:
            new_line.append(i)


    return new_line


def mapLine(line,shift):
    new_line = []

    for i in line:
        is_alpha = i.isalpha()

        if is_alpha:
            is_low = i.islower()
            if is_low:
                # get the index of the current letter in the shift
                ind = ORG.index(i)
                # alphabetic index now
                new_line.append(shift[ind])
            else:
                ind = ORG.index(i.lower())

                new_line.append(shift[ind].upper())
        else:
            new_line.append(i)


    return new_line


if __name__ == "__main__":
    # Gathering the action list needed
    result_list = firstLine()
    
    # Creating list of the shifts needed
    shifts = []

    for (encrypt,shift) in result_list:
        shifts.append(createCurrShift(encrypt,shift))
    #print("alpha:{0}".format(ORG))
    #print("current shift:{0}" .format(curr_shift))
    


    for line in sys.stdin:
        for shift in shifts:
            shift.reverse()
            first = shift.pop(0)
            if first == "m":
                # mapping else
                shift.reverse()
                line = mapLine(line,shift)
            else:
                shift.reverse()
                line = encryptLine(line,shift)
        new_line = ''.join(line).replace('\n','')
        print(new_line)


    



