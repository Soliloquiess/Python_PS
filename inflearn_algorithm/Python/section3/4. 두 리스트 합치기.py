import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
def solution(n,a,m,b):
    ans = [];
    p1=p2=0 #p1, p2는 각 a,b의 인덱스.
    c=[]    #합칠 c라는 리스트 만들어줌.
    while p1<n and p2<m: #이게 다 끝나는건 p1,p2중 하나가 다 완료되면(다돌면) 끝남
        if a[p1]<b[p2]:
            c.append(a[p1])     #c에 현 a요소가 b요소보다 작으면 a를 넣어준다.
            p1+=1
        else: #여기엔 값이 p1보다 "같거나" 작으면 실행됨.
            c.append(b[p2])
            p2+=1
    #남은 자료형 확인
    if p1<n:    #p1이 남은거(n까지 못가고 남음)
        c=c+a[p1:] #(슬라이스 사용)p1이 가리키는 곳 부터 끝까지.p1부터 마지막 자료까지 합침
    if p2<m:    #p2가 남은거(m까지 못가고 남음)
        c=c+b[p2:]
    for x in c:
        # print(x, end=' ')
        ans.append(x);
    return ans
print(solution(n,a,m,b));