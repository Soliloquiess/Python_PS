import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

# 산술평균 - 다 더해서 / n
print(round(sum(li) / n))

# 중앙값 - 오름차순 -> 중간값
li.sort()
print(li[n // 2])

# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:  # 최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

# 범위 - 최댓값-최솟값
print(max(li) - min(li))
# https://jiwon-coding.tistory.com/8


# from collections import Counter
#
# numbers = []
# for _ in range(int(input())):
#     num = int(input())
#     numbers.append(num)
#
# numbers.sort()
#
# cnt = Counter(numbers).most_common(2)
#
# print(round(sum(numbers) / len(numbers)))
# print(numbers[len(numbers) // 2])
# if len(numbers) > 1:
#     if cnt[0][1] == cnt[1][1]:
#         print(cnt[1][0])
#     else:
#         print(cnt[0][0])
# else:
#     print(cnt[0][0])
# print(max(numbers) - min(numbers))

# https://somjang.tistory.com/entry/BaekJoon-2108%EB%B2%88-%ED%86%B5%EA%B3%84%ED%95%99-Python

# import sys
# from collections import Counter
#
# n = int(sys.stdin.readline())
# li = []
# for _ in range(n):
#     li.append(int(sys.stdin.readline()))
#
# # 산술평균 - 다 더해서 / n
# print(round(sum(li) / n))
#
# # 중앙값 - 오름차순 -> 중간값
# li.sort()
# print(li[n // 2])
#
# # 최빈값 - 빈출
# cnt_li = Counter(li).most_common()#알아서 여기서 최빈값을 정렬해준다.
# if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:  # 최빈값 2개 이상
#     print(cnt_li[1][0])
# else:
#     print(cnt_li[0][0])
#
# # 범위 - 최댓값-최솟값
# print(max(li) - min(li))