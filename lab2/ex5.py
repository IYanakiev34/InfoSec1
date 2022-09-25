import sys

"""
    Insted of formathing speciifc way alsway format in base 32 this is max int size
    then chop the string into the size of the knapsack (should be power of 2 otherwise problem)
    each slice should be encyrpted to the best way possible and outputted
"""


def en():
    public_key = input().split(' ')
    public_key = [int(i) for i in public_key]
    
    for value in sys.stdin:
        value = int(value)
        value = format(value,'64b')
        chop_value = 8
        if len(public_key) == 16:
            chop_value = 16
        elif len(public_key) == 32:
            chop_value = 32
        elif len(public_key) == 64:
            chop_value = 64

        out_list = []
        for i in range(0,64,chop_value):
            chop = value[i:i+chop_value]
            out = 0
            should_print = False
            for (k,j) in zip(chop,reversed(public_key)):
                if k.isnumeric():
                    should_print = True
                    if int(k) == 1:
                        out += j
            if should_print:
                out_list.append(out)

        out_list = [str(i) for i in out_list]
        print(' '.join(out_list))
"""
    Figure how to handle decrypiton with big knapsack and with large values
"""

def de():
    first_line = input().split(' ')
    m = int(first_line[0])
    n = int(first_line[1])

    sk = input().split(' ')
    sk = [int(i) for i in sk]
    
    x = 0
    while m*x%n != 1:
        x += 1

    for value in sys.stdin:
        value = int(value)
        s = value * x % n
        bit_pat = ""
        for i in reversed(sk):
            if i <= s:
                s -= i
                bit_pat += "1"
            else:
                bit_pat += "0"
        
        out = int(bit_pat,2)
        print(out)


if __name__ == "__main__":
    """
        Input:
        e
        public key
        int value 0
        int value 1
        int value 2
        or
        d
        m n
        super increasing knapsack
        integer value 0
        integer value 1
        integer value 2
    """
    state = input()

    if state == 'e':
        en()
    else:
        de()
