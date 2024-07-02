
n = int(input())  # 첫 번째 줄: 상근이가 가진 숫자 카드의 개수
cards = set(map(int, input().split()))  # 두 번째 줄: 상근이가 가진 숫자 카드 목록
m = int(input())  # 세 번째 줄: 확인할 숫자의 개수
queries = list(map(int, input().split()))  # 네 번째 줄: 확인할 숫자 목록

# 결과를 저장할 리스트
results = []

# 집합을 사용하여 존재 여부 확인
for query in queries:
    if query in cards:
        results.append(1)
    else:
        results.append(0)

# 결과 출력
print(" ".join(map(str, results)))
