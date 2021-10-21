# def solution(arr):
#     num = list(map(int, list(str(arr))))    #이건 두자리수 이상이면 (10이면 1, 0으로 나눔)
#     num = sum(num)  #10일 경우 1+0 1이됨.
#     if arr % num == 0:
#         return True
#     else:
#         return False
#
# print(solution(10))

def solution(x):
    answer = True
    sum = 0
    t = x

    while t >= 10:
        sum += t % 10
        t = t // 10
    sum += t % 10

    return x % sum == 0

print(solution(10))
