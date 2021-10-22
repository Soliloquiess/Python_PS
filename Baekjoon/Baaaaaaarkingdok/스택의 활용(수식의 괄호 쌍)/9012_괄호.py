import sys

T = int(input())

for i in range(T):
    check = 0
    s = sys.stdin.readline().rstrip()
    for j in range(len(s)):
        if s[j] == '(':
            check += 1
        else:
            check -= 1

        if check == -1:
            answer = 'NO'
            break

    if check == 0 and s[len(s) - 1] == ')':
        answer = 'YES'
    else:
        answer = 'NO'

    print(answer)


# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')