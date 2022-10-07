if __name__ == "__main__":
    print("Hello from ex2")

    ##
    # Input:
    #   (x,y) - The original point being used
    #   a b p - y^2 = x^3 + a*x + b % p
    #   m n - the secret multipliers chosen by bob and alice
    # E.g Alice chose m => send m*(x,y)
    #     Bob chose n => send n*(x,y)
    #
    #   What to compute
    #   P' = m * (n * (x,y)) for Alice
    #   P' = n * (m * (x,y)) for Bob
    #   Return P'
    ###

    # We need a method for adding two points
    # Method for multiplying point by scalar value

    ##
    # Addition of two points given a curve E: y^2 = x^3 + a*x + b (mod p)
    # (mod p) => The whole thing mod p
    # P1 = (x1,y1) and P2 = (x2,y2) on E
    # P3 = P1 + P2
    # Algorithm:
    # ----------
    # x3 = m^2 - x1 - x2 (mod p)
    # y3 = m(x1 - x3) - y1 (mod p)
    # where m:
    # P1 != P2  then (y2 - y1)*(x2 - x1)^-1 (mod p)
    # P1 == P2 then (3x1^2 + a)*(2y1)^-1 (mod p)
    # If m == infinity then P3 = Infinity
    # infinity + P = P for all P
    ###

    # Solution steps
    # Take input
    # Calculate P = m * (n * (x,y))
    # Implement multiplication as addition
    # Return shared secret P
