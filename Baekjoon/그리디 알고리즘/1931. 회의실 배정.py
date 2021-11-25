N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)

#https://jokerldg.github.io/algorithm/2021/03/11/meeting-room.html

# n = int(input())
# s = []
# for i in range(n):
#     first, second = map(int, input().split())
#     s.append([first, second])
# s = sorted(s, key=lambda a: a[0])
# s = sorted(s, key=lambda a: a[1])
# last = 0
# cnt = 0
# for i, j in s:
#     if i >= last:
#         cnt += 1
#         last = j
# print(cnt)

#https://pacific-ocean.tistory.com/236

# import sys
#
# N = int(sys.stdin.readline())
#
# time = [[0]*2 for _ in range(N)]
# for i in range(N):
#     s, e = map(int, sys.stdin.readline().split())
#     time[i][0] = s
#     time[i][1] = e
#
# time.sort(key = lambda x: (x[1], x[0]))
#
# cnt = 1
# end_time = time[0][1]
# for i in range(1, N):
#     if time[i][0] >= end_time:
#         cnt += 1
#         end_time = time[i][1]
#
# print(cnt)

# https://suri78.tistory.com/26