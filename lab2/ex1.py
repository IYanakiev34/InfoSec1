import sys
if __name__ == "__main__":
    lines = sys.stdin.readlines()

    bytes_array = []
    for line in lines:
        for i in line:
            bytes_array.append(ord(i))

    if len(bytes_array) % 2 == 0:
        bytes_array.pop(len(bytes_array) - 1)

    key = bytes_array[:len(bytes_array)//2].copy()
    value = bytes_array[len(bytes_array)//2 + 1:].copy()

    out = []

    for (k, v) in zip(key, value):
        if v > 255:
            v = 255
        out.append(k ^ v)

    for i in out:
        sys.stdout.buffer.write(i.to_bytes(1,"little"))
