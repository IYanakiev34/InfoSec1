
import sys

def encrypt(string, key):
    keyCount = 0
    for i in range(0, len(string)):
        letter = string[i]
        if keyCount == len(key):
            keyCount = 0
            
        if key[keyCount].isupper():
            keyVal = ord(key[keyCount]) - ord('A')
        else:
            keyVal = ord(key[keyCount]) - ord('a')
            
        if letter.isalpha():
            if letter.isupper():
                val = ord(letter) - ord('A')
                val = (val + keyVal) % 26
                newlet = val + ord('A')
            else:
                val = ord(letter) - ord('a')
                val = (val + keyVal) % 26
                newlet = val + ord('a')
            keyCount += 1
            temp = list(string)
            temp[i] = chr(newlet)
            string = "".join(temp)
    
    return string



def decrypt(string, key):
    keyCount = 0
    for i in range(0, len(string)):
        letter = string[i]
        if keyCount == len(key):
            keyCount = 0
            
        if key[keyCount].isupper():
            keyVal = ord(key[keyCount]) - ord('A')
        else:
            keyVal = ord(key[keyCount]) - ord('a')
            
        if letter.isalpha():
            if letter.isupper():
                val = ord(letter) - ord('A')
                val = (val - keyVal + 26) % 26
                newlet = val + ord('A')
            else:
                val = ord(letter) - ord('a')
                val = (val - keyVal + 26) % 26
                newlet = val + ord('a')
            keyCount += 1
            temp = list(string)
            temp[i] = chr(newlet)
            string = "".join(temp)
    
    return string


    
input1 = input()
strings = []
count = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    strings.append(line)

if len(strings) > 1 and strings[1] != "":
    count = 3
method = input1.split()[0]
key = input1.split()[1]



if method == 'e':
    for string in strings:
        print(encrypt(string, key))
else:
    for string in strings:
        print(decrypt(string,key))
#if (count >= 2): 
    #print('\n', end="")

