a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

# https://pacific-ocean.tistory.com/228


# arr = input().split('-')
# s = 0
# for i in arr[0].split('+'):
#     s += int(i)
# for i in arr[1:]:
#     for j in i.split('+'):
#         s -= int(j)
# print(s)

# https://sungmin-joo.tistory.com/67