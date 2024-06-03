# 입력 받기
N, M = map(int, input().split())
baskets = [0] * N

# 공 넣기 작업 처리
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):  # 인덱스는 0부터 시작하므로 i-1에서 j까지 범위 설정
        baskets[idx] = k

# 결과 출력
print(' '.join(map(str, baskets)))
