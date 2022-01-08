# import math
# def solution(w,h):
#     return w*h - (w+h-math.gcd(w,h))

def func(w, h):
    a, b = max([w, h]), min([w, h])
    while (True):
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


def solution(w, h):
    squares = w * h
    gcd = func(w, h)

    return squares - (w + h - gcd)