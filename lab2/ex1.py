if __name__ == "__main__":
    word = input()
    toBt = ' '.join(bin(ord(x))[2:] for x in word)
    byte_list = toBt.split(' ')

    key = []
    value = []

    for i in byte_list:
        if i == "11111111":
            break
        else:
            key.append(i)

    for i in reversed(byte_list):
        if i == "11111111":
            break
        else:
            value.append(i)

    out = []
    for (k, v) in zip(key, value):
        out.append(int(k, 2) ^ int(v, 2))

    out = ''.join(format(x,'08b') for x in out)

    print(out)
