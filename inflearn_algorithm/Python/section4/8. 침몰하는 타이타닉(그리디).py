import sys
from collections import deque #deque 사용하기 위한  import
#sys.stdin=open("input.txt", "r")
n, limit=map(int, input().split())
p=list(map(int, input().split()))
def solution(n, limit, p):
    p.sort()
    p=deque(p)
    #deque는 앞에서도 넣고 뺼 수 있고 뒤에서도 넣고 뺼 수 있다.
    #리스트는 맨 앞 pop하면 앞으로 떙기는 연산해서 아주 비효율적. 이걸 안하기 위해 deque 사용.
    #즉 효율성을 위해 deque 사용하는 거. (굳이 리스트로 앞으로 땡기는 연산 안하니까)
    cnt=0
    while p:
        if len(p)==1:   #자료가 한개 남으면(한 사람이 남으면) 자료 두번 더해서 모순되므로(50인 사람 남았는데 50+50 되므로 모순)
            cnt+=1      #한개 남으면 그 혼자서 걍 보트 타고 나가면 됨.
            break       #pop 할 필요도 없이 break 실행하면 됨.
        if p[0]+p[-1]>limit:    #p의 0번 자료 + 맨 뒤자료 합해서 한계치 넘어가면
            #맨 처음 p[0]은 가장 가벼운 사람, p[-1]은 가장 무거운 사람.
            p.pop() #맨 뒷자료가 (젤 무거운 사람이) 구명보트 타고 나가버림.
            cnt+=1
        else:   #두 사람이 같이 타고 간 경우
            p.popleft() #덱 사용할떄
            # p.pop(0)  # 덱 쓸때(덱 대신 리스트 사용시
            p.pop()
            cnt+=1
    # print(cnt)
    return cnt;


print(solution(n, limit, p));

##리스트를 가지고 했는데 pop(0)으로 맨 앞 팝시키면 맨 뒤를 앞으로 이동시키는 연산
# 근데 이런걸 하고 싶지 않으면 deque라는 자료구조가 있는데 앞,뒤 둘다 넣기 가능하다
# 만약 맨 앞자료를 뺴면 리스트는 알아서 떙기는데 덱은 뺴고 떙기지 않고 다음 자료로 넘어간다.


###위에서도 덱 썼지만 덱 안쓰고 리스트만 쓰는 경우

# import sys
# from collections import deque #deque 사용하기 위한  import
# #sys.stdin=open("input.txt", "r")
# n, limit=map(int, input().split())
# p=list(map(int, input().split()))
# p.sort()
# p=deque(p)
# #deque는 앞에서도 넣고 뺼 수 있고 뒤에서도 넣고 뺼 수 있다.
# #리스트는 맨 앞 pop하면 앞으로 떙기는 연산해서 아주 비효율적. 이걸 안하기 위해 deque 사용.
# #즉 효율성을 위해 deque 사용하는 거. (굳이 리스트로 앞으로 땡기는 연산 안하니까)
# cnt=0
# while p:
#     if len(p)==1:   #자료가 한개 남으면(한 사람이 남으면) 자료 두번 더해서 모순되므로(50인 사람 남았는데 50+50 되므로 모순)
#         cnt+=1      #한개 남으면 그 혼자서 걍 보트 타고 나가면 됨.
#         break       #pop 할 필요도 없이 break 실행하면 됨.
#     if p[0]+p[-1]>limit:    #p의 0번 자료 + 맨 뒤자료 합해서 한계치 넘어가면
#         #맨 처음 p[0]은 가장 가벼운 사람, p[-1]은 가장 무거운 사람.
#         p.pop() #맨 뒷자료가 (젤 무거운 사람이) 구명보트 타고 나가버림.
#         cnt+=1
#     else:   #두 사람이 같이 타고 간 경우
#         p.popleft() #덱 사용할떄
#         # p.pop(0)  # 덱 쓸때(덱 대신 리스트 사용시
#         p.pop()
#         cnt+=1
# print(cnt)
