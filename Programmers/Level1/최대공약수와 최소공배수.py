def gcd(n,m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n, m)
    else:
        return n

def solution(n,m):
    return [gcd(n,m),int(m*n/gcd(n,m))]


print(solution(2,5))
#https://velog.io/@richeberry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4python-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98