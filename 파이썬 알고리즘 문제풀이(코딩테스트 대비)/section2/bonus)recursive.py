def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return solution(n-1) + \
               solution(n-2) + \
               solution(n-3)

# t = int(input())
# for _ in range(t):
#     print(solution(int(input())))
# 이 3줄은 왜 적혀있는지 모르겠다.

print(solution(5));


##########
# def func(data):
#     if data == 1:
#         return 1
#     elif data == 2:
#         return 2
#     elif data == 3:
#         return 4
#

# f(5)인 경우 f(4)+ f(3)+f(2)이며 이 경우
# f(4)에서의 값 7+ f(3)에서의 값 4 + f(2)에서의 값 2를 더해서 13이 나온다.
#     return func(data - 1) + func(data - 2) + func(data - 3)
## func(5)



