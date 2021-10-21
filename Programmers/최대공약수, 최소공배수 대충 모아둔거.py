# def LCM(X, Y):
#     if X<Y:
#         max = Y
#     else:
#         max = X
#     for i in range(max,(X*Y)+1):
#         if i%X==0 and i%Y==0:
#             res = i
#             break
#     return res
#
#
# X, Y = list(map(int,input().split()));
#
# print(LCM(X,Y))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

#이건 최소공배수 유클리드 호제법 이용
def lcm(a, b):
    return a * b // gcd(a, b)


X, Y = list(map(int,input().split()));

print(lcm(X,Y))

# print(UC(1, 1));

# def GCD(X, Y):
#   근데 이렇게 하면 1, 1을 못찾네
#     if X<Y:
#         min = X
#     else:
#         min = Y
#     for i in range(min+1,1,-1):
#         if X%i==0 and Y%i==0:
#             res = i
#             break
#     return res
# print(gcd(1, 1));


# def gcd(p, q):
#     if(n>=m):
#         i=m;
#
#     else :
#         i=n;
#     for j in range(1,i+1):
#         if(n%j ==0 and m%j ==0):
#             gcd_v =j;
#     return gcd_v
#
#
# n, m = list(map(int,input().split()));
# print(gcd(n,m));


# 3. 최대공약수와 최소공배수 관계
# 유클리드 호제법을 활용하여 최소공배수를 쉽게 구할 수 있습니다.
# 예를 들어, X = AB, Y = BC라고 했을 때 X와 Y의 최대공약수는 B, 최소공배수는 ABC입니다.
# X와 Y를 곱하면 AB^2C이니까 최대공약수 B로 나누면 최소공배수 ABC가 나옵니다.
# 위의 유클리드 호제법을 이용한 최대공약수를 구하는 코드는 아래와 같습니다.
#

#이걸 최소공배수는 UC(gcd)가 있어야 최소공배수를 구하기가 가능하다.
# #유클리드 호제법을 이용한 최대공약수 구하기
# def UC(X, Y):
#     while(Y):
#         X, Y = Y, X%Y
#     return X
#
# #유클리드 호제법을 이용한 최소공배수 구하기
# def UC2(X, Y):
#     result = (X*Y) // UC(X,Y)
#     return result




###

# 최대 공약수,
# 최대 공약수란, 숫자 a, b가 주어졌을 떄, 공통되는 약수 중에서 최대 값을 의미한다.
#
# 최대공약수 구하기.
# 1. a, b 각각의 약수를 구해서 공통되는 약수중에서 가장 큰 값을 찾는 방법.
# 찾지 않아도 되는 약수들 까지 구해야하기 때문에 효율적이지 않다.
# 2. 유클리드 호제법
# 유클리드 호제법이란,
# 숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b 의최대 공약수 는 a 와 b 의 최대 공약수 가 같다는 것을 의미한다.
#
# 그럼, 계속해서 a 를 b로 나누어서 b를 a에 나눈 나머지를 b 에 대입시켜서 b 가 0이 될때 까지 반복을
# 하면, 남는 a 값이 바로 최대 공약수 이다.

# 코드
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# 최소공배수
# 서로 다른 수 a, b의 배수중에서 공통되는 배수 중에 가장 작은 값을 의미한다.
#
# 최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누면 나오게 된다.
#
# (최소공배수 x 최대 공약수) = `gcd^2 * m * n [m, n은 서로수]` => a * b
# 를 이용한 방법이다.

# def lcm(a, b):
#     return a * b / gcd(a, b)