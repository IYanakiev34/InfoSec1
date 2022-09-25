import sys
import math

if __name__ == "__main__":
    
    """
        Input:
        m,n: 41, 491
        [private key]: 2 3 7 14 30 57 120 251
        public key: 83 123 287 83 248 373 10 471
    """

    """
       m,n are relatively prime: n  is a number > wn+ n r.g(251 + sum of eight before this) 491, m is multiplication constant e.g 41
       public key ki = m * wi % n
    """
    # check if m and n are relatively prime
    first_line = input().split(',')
    first_line = first_line[0].split(' ')
    first_line = [int(i) for i in first_line]
    
    if math.gcd(first_line[0],first_line[1]) != 1:
        print(-1)
        sys.exit()
    
    # check validity of private key
    private_key = input().split(' ')
    private_key = [int(i) for i in private_key]

    curr_sum = 0
    for index,i in enumerate(private_key):
        if curr_sum >= i:
            print(-1)
            sys.exit()
        else:
            if index != (len(private_key) - 1):
                curr_sum += i

    # check if n > private_key[len(private_key) - 1] + curr_sum
    if first_line[1] <= private_key[len(private_key) - 1] + curr_sum:
        print(-1)
        sys.exit()

    # n is greater than
    # get public key
    public_key =  input().split(' ')
    public_key = [int(i) for i in public_key]
    
    if len(public_key) < len(private_key):
        print(0)
        sys.exit()

    for (i,j) in zip(public_key,private_key):
        if i != ((first_line[0] * j) % first_line[1]):
            print(0)
            sys.exit()
    
    print(1)



