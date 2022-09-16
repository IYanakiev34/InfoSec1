#lowerbound = input()
#upperbound = input()
ciphertext = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    ciphertext += line

alphabet = []
for i in range(0,26):
    alphabet.append(0)

newtext = ""
for i in range(len(ciphertext)):
    if ciphertext[i].isalpha():
        newtext += ciphertext[i]

#for i in range(int(lowerbound), (int(upperbound)+1)):
i = 5
array = []
for j in range(i):
    array.append(alphabet)

for j in range(i):
    factor = j
    index = factor
    while index < len(newtext):
        letter = newtext[index]
        if letter.isupper():
            val = ord(letter) - ord('A')
        else:
            val = ord(letter) - ord('a')
        array[j][val] += 1
        factor += 1
        index = (factor*i)-1


print(array)
    
            
        
