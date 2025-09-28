def solution(n):
    k = 1
    while True:
        if (6 * k) % n == 0:
            return k
        k += 1
