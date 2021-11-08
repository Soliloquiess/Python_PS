import sys
#sys.stdin=open("input.txt", "r")
n, m=map(int, input().split()) #n이 자료의 크기 m이 찾고자 하는 수
a=list(map(int, input().split())) #

def solution(n,m,a):
    a.sort()
    lt=0 #왼쪽 맨 끝줄
    rt=n-1  #오른쪽 맨 끝줄
    while lt<=rt:   #lt가 rt보다 크면 이분탐색 종료.
        mid=(lt+rt)//2;
        if a[mid]==m:
            print(mid+1)    #답으로는 +1해서 인덱스 출력해줘야.
            break;
        elif a[mid]>m:      #mid가 m보다 크면 mid보다 작은쪽(앞)에 있으므로 rt하나 줄여야
            rt=mid-1;
        else:               #그렇지 않으면 내가 찾고자 하는 값이 중간지점보다 더 큰 쪽에 있는 거.
            lt=mid+1;


print(solution(n,m,a));