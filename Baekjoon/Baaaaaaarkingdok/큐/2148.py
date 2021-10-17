from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while (len(deque) > 1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])

# 이건 규칙 찾은거
# a = int(input())
# b = 2
# while True:
#     if a == 1 or a == 2:
#         print(a)
#         break
#     b *= 2
#     if b >= a:
#         print((a - (b // 2)) * 2)
#         break
#https://pacific-ocean.tistory.com/61