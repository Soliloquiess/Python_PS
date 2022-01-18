# def solution(people, limit) :
#     people.sort()
#     cnt = 0;
#     i = 0; j = len(people)-1
#     while i<=j :
#         cnt+=1
#         if people[j]+people[i]<=limit :
#             i+=1
#         j-=1
#     return cnt

from collections import deque

def solution(people, limit):
    boat = 0
    people.sort()

    # 보트는 2명씩만 탈 수 있고 무게 제한도 있음.
    q = deque(people)
    w = 0
    cnt = 0
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                boat += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                boat += 1
        else:
            if q[0] <= limit:
                q.pop()
                boat += 1
    return boat

print(solution([70, 50, 80, 50],100));
print(solution([70, 80, 50],100));
