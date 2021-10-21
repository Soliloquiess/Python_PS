from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idxs = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

count = 0
for idx in idxs:
    while True:
        if dq[0] == idx:
            dq.popleft()
            break
        else:
            if dq.index(idx) < len(dq)/2:
                while dq[0] != idx:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != idx:
                    dq.appendleft(dq.pop())
                    count += 1
print(count)

# from collections import deque
#
# n, m = map(int, input().split())
# target_indexes = list(map(int, input().split()))
# cnt = 0
# arr = deque([i for i in range(1, n + 1)])
#
#
# def compare_min_length(target):
#     global arr
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i, len(arr) - i - 1
#
#
# def front_rotate(target, cnt):  # 왼쪽으로 이동
#     global arr
#     while True:
#         if arr[0] == target:
#             arr.popleft()
#             return cnt
#         arr.append(arr.popleft())
#         cnt += 1
#
#
# def back_rotate(target, cnt):  # 오른쪽으로 이동
#     global arr
#     while True:
#         if arr[0] == target:
#             arr.popleft()
#             return cnt
#         arr.appendleft(arr.pop())
#         cnt += 1
#
#
# for target in target_indexes:
#     front, back = compare_min_length(target)
#     if front <= back:
#         temp_cnt = front_rotate(target, cnt)
#     else:
#         temp_cnt = back_rotate(target, cnt)
#     cnt = temp_cnt
# print(cnt)

# n, m = map(int, input().split())
# s = list(map(int ,input().split()))
# q = [i for i in range(1, n + 1)]
# cnt = 0
# for i in range(m):
#     q_len = len(q)
#     q_index = q.index(s[i])
#     if q_index < q_len - q_index:
#         while True:
#             if q[0] == s[i]:
#                 del q[0]
#                 break
#             else:
#                 q.append(q[0])
#                 del q[0]
#                 cnt += 1
#     else:
#         while True:
#             if q[0] == s[i]:
#                 del q[0]
#                 break
#             else:
#                 q.insert(0, q[-1])
#                 del q[-1]
#                 cnt += 1
# print(cnt)


#rotate 함수 사용법
# from collections import deque
# items = deque([1, 2])
# items.append(3)        # deque == [1, 2, 3]
# items.rotate(1)        # The deque is now: [3, 1, 2]
# items.rotate(-1)       # Returns deque to original state: [1, 2, 3]
# item = items.popleft() # deque == [2, 3]
# http://daplus.net/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%AA%A9%EB%A1%9D%EC%9D%84-%ED%9A%8C%EC%A0%84%EC%8B%9C%ED%82%A4%EB%8A%94-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-%EB%B0%A9%EB%B2%95/