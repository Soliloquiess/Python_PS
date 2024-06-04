# N과 M을 입력받습니다.
N, M = map(int, input().split())

# 바구니를 1번부터 N번까지 초기화합니다.
baskets = list(range(1, N + 1))

# M번의 명령을 입력받아 처리합니다.
for _ in range(M):
    i, j = map(int, input().split())
    # i부터 j까지의 부분을 역순으로 만듭니다. (리스트 슬라이싱 활용)
    baskets[i-1:j] = reversed(baskets[i-1:j])

# 최종 결과를 출력합니다.
print(' '.join(map(str, baskets)))


# # N과 M을 입력받습니다.
# N, M = map(int, input().split())
# 
# # 바구니를 1번부터 N번까지 초기화합니다.
# baskets = list(range(1, N + 1))
# 
# # M번의 명령을 입력받아 처리합니다.
# for _ in range(M):
#     i, j = map(int, input().split())
#     # i부터 j까지의 부분을 역순으로 바꾸기 위해 직접 교환합니다.
#     left = i - 1
#     right = j - 1
#     while left < right:
#         # left와 right 위치의 요소를 교환
#         baskets[left], baskets[right] = baskets[right], baskets[left]
#         left += 1
#         right -= 1
# 
# # 최종 결과를 출력합니다.
# for basket in baskets:
#     print(basket, end=' ')
