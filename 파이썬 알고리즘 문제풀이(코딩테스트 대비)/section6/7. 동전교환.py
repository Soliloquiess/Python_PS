import sys
# sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global res
    if L>=res:  #이 레벨(L)이 계속 깊이탐색rka.
        #우리가 답으로 갖던게 res보다 크면 그 가닥 볼 필요도 없어서 바로 리턴(최소여야되니까)
        return
    if sum>m:   #sum이 우리가 거슬려주러는 금액보다 커지면 종료
        return
    if sum==m:  #sum이 누적했는데 m이 되면 답 찾은거
        if L<res:   #L이 답
            res=L
    else:
        for i in range(n):  #동전 개수만큼 돔 (n만큼)
            DFS(L+1, sum+a[i])  #레벨은 1씩 증가
    return res;

if __name__=="__main__":
    n=int(input())  #동전의 종류 개수
    a=list(map(int, input().split()))   #동전의 종류들을 a라는 리스트에 받음.
    m=int(input())  #우리가 만들고자 하는 거스름돈.
    res=2147000000  #최소니까 큰 값으로 넣음(minimum과 같음)
    a.sort(reverse=True)#1원짜리 쭉 들어가면 너무 깊이들어감
    #근데 내림차순 하면 어떻게하든 5원짜리부터 들어감(1,2,5)순에서 (5,2,1)순이므로
    #5원부터 탐색하게 하면 시간복잡도를 확 줄이기가 가능하다.(아니면 앞에 1원부터 하면 존나 오래걸렸을것)
    print(DFS(0, 0))
    print(res)
