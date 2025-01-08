N = int(input())  # 참가자 수
max_prize = 0  # 가장 많은 상금

for _ in range(N):
    a, b, c = map(int, input().split())
    
    if a == b == c:  # 같은 눈이 3개
        prize = 10000 + a * 1000
    elif a == b or a == c:  # 같은 눈이 2개
        prize = 1000 + a * 100
    elif b == c:  # 같은 눈이 2개
        prize = 1000 + b * 100
    else:  # 모두 다른 눈
        prize = max(a, b, c) * 100
    
    max_prize = max(max_prize, prize)

print(max_prize)
