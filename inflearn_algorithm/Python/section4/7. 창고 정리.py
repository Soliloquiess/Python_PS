import sys
#sys.stdin=open("input.txt", "r")
L=int(input())
a=list(map(int, input().split()))
m=int(input())
def solution(L,a,m):
    a.sort()    #오름차순 정렬시 맨 앞자리가 가장 낮은 곳의 높이 맨뒤가 젤 높은 곳.
    #가장 낮은곳은 +1, 높은곳은 -1 해주면 되지 않을까?
    #조정하면  또 정렬. 이걸 입력 횟수만큼(m) 반복후 마지막에 맨 뒤에값에서 맨 앞의 값을 뺴주면 됨.
    for _ in range(m):#m회 높이 조정
        a[0]+=1 #맨 앞(제일 낮은곳 +1)
        a[L-1]-=1   #맨 뒤(제일 높은곳 -1)
        a.sort() #계속 정렬

    #print(a[L-1]-a[0])      #최대높이에서 최소값 뺴주면 됨.
    return a[L-1]-a[0];
print(solution(L,a,m));