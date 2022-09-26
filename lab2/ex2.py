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
        bytes_array +=(list(line))
    
    # print("\nBytes array before filtering:\n{0}\n" .format(bytes_array))

    for index,i in enumerate(bytes_array):
        if i == 195 and bytes_array[index+1] == 191:
            bytes_array[index+1] = 255
            bytes_array.pop(index)
    # print("\nBytes array after filtering:\n{0}\n" .format(bytes_array))
    
    key = []
    value = []
    first_y = -1
    
    for index,i in enumerate(bytes_array):
        if i == 255 and first_y == -1:
            first_y = index
            break

    key = bytes_array[:first_y].copy()
    value = bytes_array[first_y+1:].copy()


    keystream = get_keystream(key)
    # discard phase
    for i in range(0,256):
        c = next(keystream)

    out = []
    for c in value:
        val = c ^ next(keystream)
        out.append(val)
        

    for i in out:
        if i <= 255:
            sys.stdout.buffer.write(i.to_bytes(1, "little"))

