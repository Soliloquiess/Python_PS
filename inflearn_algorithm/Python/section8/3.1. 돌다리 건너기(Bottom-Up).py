import sys
# sys.stdin = open("input.txt", 'r')
n=int(input())
def solution(n):
    dy=[0]*(31)
    dy[1]=1
    dy[2]=2
    for i in range(3, n+2):
        dy[i]=dy[i-1]+dy[i-2]

    print(dy[n+1])
    return dy[n+1];

print(solution(n));


#재귀 쓰면서도 메모이제이션으로 넣어가면서 컷 해가면서 쓰는게 동적계획법이라 보기도 하고
#재귀가 뻗어나가는게 점화식이랑 비슷하니까 넓은 의미에서 동적계획법이라 부르기도 하고
#그렇지만 작은거에서 점점 큰 문제로 뻗어나가는 bottom-up 방식이 진짜 동적 계획법이다.
#탑다운 방식 메모이제이션은 넓은 의미에서의 동적계획법이다.

# 덤 풀이)

# def dfs(k):
#     if dy[k]>0:
#         return dy[k]
#     if k==1 or k==2:
#         return k
#     else :
#         dy[k]=dfs(k-1) +dfs(k-2)
#         return dy[k]
#
# if __name__=='__main__':
#     n=int(input())
#     dy=[0]*(n+1)
#     s=0
#     dfs(n)
#     s+=dy[-1]+dy[-2]
#     print(s)