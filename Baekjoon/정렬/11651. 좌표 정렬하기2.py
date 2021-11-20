import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

s_array = sorted(array)

for y, x in s_array:
    print(x, y)

#https://wook-2124.tistory.com/473

# import sys
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     so.append(list(map(int, sys.stdin.readline().split())))
# so.sort(key=lambda x: (x[1], x[0]))
# for i in so:
#     print(i[0], i[1])
#
# # https://pacific-ocean.tistory.com/140