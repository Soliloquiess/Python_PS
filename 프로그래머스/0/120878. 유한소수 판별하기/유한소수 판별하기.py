def solution(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    g = gcd(a, b)
    b //= g

    for p in [2, 5]:
        while b % p == 0:
            b //= p

    return 1 if b == 1 else 2
