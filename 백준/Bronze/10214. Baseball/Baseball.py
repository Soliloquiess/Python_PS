T = int(input())  
results = []

for _ in range(T):
    yonsei_score = 0
    korea_score = 0
    for _ in range(9):
        Y, K = map(int, input().split())
        yonsei_score += Y
        korea_score += K
    if yonsei_score > korea_score:
        results.append("Yonsei")
    elif yonsei_score < korea_score:
        results.append("Korea")
    else:
        results.append("Draw")

for result in results:
    print(result)
