n = int(input())
results = []

for _ in range(n):
    r, e, c = map(int, input().split())  # r: 광고 안 했을 때 수익, e: 광고 했을 때 수익, c: 광고 비용
    profit_difference = e - c  # 순수익

    if r < profit_difference:
        results.append("advertise")
    elif r > profit_difference:
        results.append("do not advertise")
    else:
        results.append("does not matter")

for result in results:
    print(result)