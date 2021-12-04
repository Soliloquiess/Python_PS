import sys

input = sys.stdin.readline

# 숫자 N
N = int(input())

# 0의 개수
count = 0

# N이 5 이상이면 while문 돌려
while N >= 5:
    # 5로 나눈 몫은 0의 개수가 되고,
    count += N // 5

    # 5가 2번있는 것은 2개 증가를 위해
    N //= 5

print(count)

#https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1676%EB%B2%88-%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC-0%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython


# N = int(input())
# print(N//5 + N//25 + N//125)

#https://hwiyong.tistory.com/360