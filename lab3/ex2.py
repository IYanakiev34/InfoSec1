import collections


def inv(n, q):
    return egcd(n, q)[0] % q


def egcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b > 0:
        q, r = divmod(a, b)
        a, b = b, r
        s0, s1, t0, t1 = s1, s0 - q * s1, t1, t0 - q * t1
    return s0, t0, a


Coord = collections.namedtuple("Coord", ["x", "y"])


class ElCurv(object):
    def __init__(self, a, b, q):
        self.a = a
        self.b = b
        self.q = q
        self.zero = Coord(0, 0)

    def add(self, point1, point2):
        if point1 == self.zero:
            return point2
        if point2 == self.zero:
            return point1
        if point1.x == point2.x and (point1.y != point2.y or point1.y == 0):
            return self.zero
        if point1.x == point2.x:
            line = (
                (3 * point1.x * point1.x + self.a) * inv(2 * point1.y, self.q) % self.q
            )
        else:
            line = (point2.y - point1.y) * inv(point2.x - point1.x, self.q) % self.q

        x = (line * line - point1.x - point2.x) % self.q
        y = (line * (point1.x - x) - point1.y) % self.q
        return Coord(x, y)

    def mult(self, p, n):
        res = self.zero
        point2 = p
        while 0 < n:
            if n & 1 == 1:
                res = self.add(res, point2)
            n, point2 = n >> 1, self.add(point2, point2)
        return res


if __name__ == "__main__":

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

    # Bacause of stupid themis cant do one liner :((()))
    point = input()
    point = point.replace("(", "").replace(")", "").split(",")
    point = [int(i.replace(" ", "")) for i in point]
    point = Coord(point[0], point[1])
    par = input().split(" ")
    a = int(par[0])
    b = int(par[1])
    p = int(par[2])
    par = input().split(" ")
    m = int(par[0])
    n = int(par[1])

    curv = ElCurv(a, b, p)

    new_point = curv.mult(point, m)
    final_point = curv.mult(new_point, n)

    print("({0}, {1})".format(final_point.x, final_point.y))
