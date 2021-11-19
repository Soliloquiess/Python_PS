# t = int(input())
# for i in range(t):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     rs = r1 + r2
#     rm = abs(r1 - r2)
#     if d == 0:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#     else:
#         if d == rs or d == rm:
#             print(1)
#         elif d < rs and d > rm:
#             print(2)
#         else:
#             print(0)


import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외에
#https://ooyoung.tistory.com/111


# n = int(input())
#
# for i in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
#     R = [r1, r2, r]
#     m = max(R);
#     R.remove(m)
#     print(-1 if (r == 0 and r1 == r2) else 1 if (r == r1 + r2 or m == sum(R)) else 0 if (m > sum(R)) else 2)

# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-1002%EB%B2%88-%ED%84%B0%EB%A0%9B-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%EB%93%9C-%EB%B0%8F-%EC%84%A4%EB%AA%85