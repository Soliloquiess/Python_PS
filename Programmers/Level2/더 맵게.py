# def solution(scoville, k):
#     mix_cnt = 0
#     while min(scoville) < k:
#         scoville.sort()
#         try:
#             scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
#         except IndexError:
#             return -1
#         mix_cnt += 1
#
#     return mix_cnt
#https://itholic.github.io/kata-more-spicy/


import heapq

def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1
    return mix_cnt

print(solution([1, 2, 3, 9, 10, 12], 7))


#덤
#https://www.daleseo.com/python-heapq/

# import heapq
#
# # 최소 힙 생성, push
# heap_list = []
# heapq.heappush(heap_list, 4)
# heapq.heappush(heap_list, 1)
# heapq.heappush(heap_list, 7)
#
# # pop
# heapq.heappop(heap_list)
#
# # pop하지 않고 최솟값 얻기
# print(heap_list[0])
#
# # 기존 리스트를 힙으로 변환
# a_list = [4, 1, 7, 3, 8, 5]
# heapq.heapify(a_list)