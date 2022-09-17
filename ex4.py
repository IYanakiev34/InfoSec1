import sys


def getFirstLine():
    line = input().split(' ')

    action = ''
    value = ''

    for index, i in enumerate(line):
        if index % 2 == 0:
            action = i
        elif index % 2 == 1:
            value = i

    return (action, value)


def encryptLetter(letter, action, value, index_value):

    if action == 'e':
        # print("index of value:{0} and the value[index% len(value)]:{1}" .format(
        #    index_value % len(value), value[index_value % len(value)]))
        # print("ord('a'):{0}, letter:{1} ord(letter):{2}, ord(value[index_value % len(value)]):{3}" .format(
        #    ord('a'), letter, ord(letter), ord(value[index_value % len(value)])))
        letter = chr(ord('a') + (ord(letter) - ord('a') +
                     (ord(value[index_value % len(value)]) - ord('a'))) % 26)
    else:
        letter = chr(ord('a') + (ord(letter) - ord('a') + (26 -
                     (ord(value[index_value % len(value)]) - ord('a')))) % 26)

    return letter


def applyShift(line, action, value):
    new_line = [None]*len(line)
    value_index = 0

    for index,i in enumerate(line):
        if i.isalpha():
            if i.islower():
                new_line[index] = encryptLetter(i, action, value, value_index)
                value_index += 1
            elif i.isupper():
                new_line[index] = encryptLetter(
                    i.lower(), action, value, value_index)
                new_line[index] =new_line[index].upper()
                value_index += 1
            # print("The index is:{0} and the new_line[index]:{1}" .format(
            #   value_index % len(value), new_line[index]))
        else:
            new_line[index] = i
    
    return new_line


if __name__ == "__main__":
    (action, value) = getFirstLine()

    # Do something with the action or value on the text
    for line in sys.stdin:
        line = applyShift(line, action, value)
        
        # print("The new line is:{0}" .format(''.join(line).replace('\n','')))
        print(''.join(line).replace('\n',''))
        



