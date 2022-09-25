from sre_parse import fix_flags
import unicodedata
import sys


def KSA(key):
    S = list(range(256))

    j = 0
    for i in range(0, 256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]

        # Return generator
        yield K


def get_keystream(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == "__main__":
    lines = sys.stdin.buffer.readlines()
    
    bytes_array = []
    for line in lines:
        readable = line.decode('utf-8')
        print(readable)
        for i in readable:
            bytes_array.append(ord(i))

    print(bytes_array)

    
    # keystream = get_keystream(key)

    
    # discard phase
    #for i in range(0, 256):
        # c = next(keystream)

    # out = []
    # for c in value:
        # val = c ^ next(keystream)
        # out.append(val)


