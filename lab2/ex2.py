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
    lines = sys.stdin.readlines()
    bytes_array = []
    for line in lines:
        for i in line:
            bytes_array.append(ord(i))

    # print("Bytes array:{0}\n" .format(bytes_array))
    # bytes_array.pop(len(bytes_array) - 1)
    key = []
    value = []
    
    first_index = -1
    for i in bytes_array:
        # Thanks to stupid themis :))))) FIX IT PLEASE
        if i == 56575:
            i = 255

        if first_index == -2:
            value.append(i)

        if i == 255 and first_index == -1:
            first_index = -2
        elif i != 255 and first_index == -1:
            key.append(i)

    # print("\nkey:\n{0}\nvalue:\n{1}\n" .format(key, value))

    keystream = get_keystream(key)
    # discard phase
    for i in range(0,256):
        c = next(keystream)

    out = []
    for c in value:
        val = c ^ next(keystream)
        out.append(val)
        
    hexes = []
    for i in out:
        hexes.append(hex(i))

    # print("\n{0}\n" .format(hexes))
    # print("\n{0}\n" .format(out))

    for i in out:
        if i <= 255:
            sys.stdout.buffer.write(i.to_bytes(1, "little"))
        else:
            sys.stdout.buffer.write(i.to_bytes(2, "little"))


# y => 195,191
