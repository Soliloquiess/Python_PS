import sys

n = int(input())
b = list(map(int, input().split()))

a = sorted(b)


def search(a, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if(a[mid] == target):
        return mid
    elif (a[mid] > target):
        return search(a, target, low, mid-1)
    else:
        return search(a, target, mid+1, high)


for i in b:
    target = i
    print(search(a, target, 0, n), end=' ')



# https://ohdowon064.tistory.com/155

# n = int(input())
# # 입력 처리
# data = list(map(int, input().split()))
#
# # binary search 함수
# def bin_search(data, start, end, k):
#     while start <= end:
#         mid = (start + end) // 2
#         if data[mid] == k:
#             return mid
#         elif data[mid] < k:
#             start = mid + 1
#         else:
#             end = mid - 1
#
# # 데이터의 각 원소에 오름차순 순위 부여
# def resort(data):
#     index_memo = ""
#     sorted_data = sorted(data)
#     for i in data:
#         index_memo += str(bin_search(sorted_data, 0, len(data)-1, i)) + " "
#     return index_memo
#
# # 결과값 출력
# print(resort(data))
#
