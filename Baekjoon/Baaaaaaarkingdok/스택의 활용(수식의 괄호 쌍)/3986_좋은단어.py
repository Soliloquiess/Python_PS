# def check(word):
#     temp = []
#     for i in range(len(word)):
#         if temp and temp[-1] == word[i]:
#             temp.pop()
#         else:
#             temp.append(word[i])
#     if not temp:
#         return True
#     else:
#         return False
#
#
# n = int(input())
# result = 0
#
# for _ in range(n):
#     data = input()
#     if check(data):
#         result += 1
#
# print(result)


'''
괄호랑 비스하다. 스택으로 풀이
'''
N=int(input())
cnt=0
for _ in range(N):
    S = list(input())
    stack=[]
    for i in S:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:   #스택 안 비었으면 실행 안함.
        cnt+=1
print(cnt)


