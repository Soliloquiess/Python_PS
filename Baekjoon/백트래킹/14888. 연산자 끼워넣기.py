from itertools import permutations

n = int(input())
o = ['+', '-', '*', '/']
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # + - * /
oper = []
oper = []
for i in range(4):
    for j in range(op[i]):
        oper.append(o[i])

oper = list(set(permutations(oper, len(oper))))  # 중복제거

answer = []
for i in oper:
    n = num[0]
    for j in range(len(num) - 1):
        if i[j] == '+':
            n += num[j + 1]
        elif i[j] == '-':
            n -= num[j + 1]
        elif i[j] == '*':
            n *= num[j + 1]
        else:
            if n // num[j + 1] < 0:
                n = -(-n // num[j + 1])
            else:
                n = n // num[j + 1]

    answer.append(n)
print(max(answer))
print(min(answer))
# 8. 입력받은 연산자의 숫자를 이용하여 해당하는 연산자의 개수만큼 리스트에 저장
#
# 12. 순열을 이용하여 모든 경우의 수를 만들고, set을 이용하여 중복을 제거해준다.
#
# 15. 연산자 경우의 수 모두 비교
#
# 24. 나눗셈의 경우에는 음수일 경우, 양수로 변경해준뒤 다시 음수로 만들어주는 과정을 진행한다.
#
#      왜냐하면 -1/3인 경우는 반올림을 하게되면 -1로 나오므로 제대로 계산해주기 위함.
#
# 31. 최대값과 최솟값 출력
# https://jiwon-coding.tistory.com/88



#이건 이렇게 쉽게 풀었지만 다들 DFS, 백트래킹을 이용해서 많이들 푸셨다.

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
#
# nums = list(map(int, input().split()))
#
# a, b, c, d = map(int, input().split())
#
# max_ans, min_ans = -sys.maxsize - 1, sys.maxsize
#
#
# def solution(num, idx, add, sub, mul, div):
#     global max_ans, min_ans
#     if idx == N:
#         max_ans = max(max_ans, num)
#         min_ans = min(min_ans, num)
#         return
#
#     if add > 0:
#         solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
#     if sub > 0:
#         solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
#     if mul > 0:
#         solution(num * nums[idx], idx + 1, add, sub, mul - 1, div)
#     if div > 0:
#         solution(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)
#
#
# solution(nums[0], 1, a, b, c, d)
# print(max_ans)
# print(min_ans)
#
#
# https://chul2-ing.tistory.com/67