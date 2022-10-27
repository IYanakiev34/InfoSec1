
from sBoxes import t1, t2, t3, t4

a = 0x0123456789ABCDEF 
b = 0xFEDCBA9876543210 
c = 0xF096A5B4C3B2E187
vals = [a,b,c]

def round(a, b, c, x, mul):
    c = c ^ x
    a -= t1[c[0:8]] ^ t2[c[16:24]] ^ t3[c[32:40]] ^ t4[c[48:56]]
    b += t4[c[8:16]] ^ t3[c[24:32]] ^ t2[c[40:48]] ^ t1[c[56:64]]
    b *= mul


def feedforward(vals, saveVals):
    vals[0] *= saveVals[0]
    vals[1] -= saveVals[1]
    vals[2] += saveVals[2]
    return vals

def passer(a,b,c,mul,bytes):
    round (a,b,c, bytes[0] ,mul)
    round(b,c,a, bytes[1] ,mul)
    round(c,a,b, bytes[2] ,mul)
    round (a,b,c, bytes[3] ,mul)
    round (b,c,a, bytes[4], mul)
    round(c,a,b, bytes[5],mul)
    round(a,b,c, bytes[6] ,mul)
    round(b,c,a, bytes[7] ,mul)
    return [a,b,c]


def keySchedule(bytes):
    bytes[0] -= bytes[7] * 0xA5A5A5A5A5A5A5A5
    bytes[1] ^= bytes[0]
    bytes[2] += bytes[1]
    bytes[3] -= bytes[2] ^ ((bytes[1])<<19)
    bytes[4] *= bytes[3]
    bytes[5] += bytes[4]
    bytes[6] -= bytes[5] ^ ((bytes[4])>>23)
    bytes[7] ^= bytes[6]
    bytes[0] += bytes[7]
    bytes[1] -= bytes[0] ^ ((bytes[7])<<19)
    bytes[2] ^= bytes[1]
    bytes[3] += bytes[2]
    bytes[4] -= bytes[3] ^ ((bytes[2])>>23)
    bytes[5] ^= bytes[4]
    bytes[6] += bytes[5]
    bytes[7] -= bytes[6] ^ 0x0123456789ABCDEF;


def hash(list, vals):
    saveVals = vals.copy()
    bytes = []
    for i in range(0, 512, 64):
        bytes.append(hex(int(list[i:i+64], base=2)))
    
    vals = passer(vals[0], vals[1], vals[2], 5, bytes)
    keySchedule(bytes)
    vals = passer(vals[0], vals[1], vals[2], 7, bytes)
    keySchedule(bytes)
    vals = passer(vals[0], vals[1], vals[2], 9, bytes)
    vals = feedforward(vals, saveVals)
    
        
        

# Taking in the input and padding
input = input()
length = len(input)
len2 = length+1
inn = []
for i in input:
    inn.append(format(ord(i), '08b'))
inn.append(format(1, '08b'))

while len2 % 64 != 56:
    len2 += 1
    inn.append(format(0, '08b'))

inn.append(format(length*8, '064b'))
inn = ''.join(inn)

# Starting the hash
for i in range(0,len(inn),512):
    hash(inn[i:i+512], vals)
