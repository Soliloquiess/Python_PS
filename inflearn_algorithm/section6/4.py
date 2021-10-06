import sys
#sys.stdin=open("input.txt", "r")
def DFS(L, sum):

#L이 n이 되면 종료.0번부터니까 n-1까지 돌고 n이 되면 종료.
#이 sum이라는 것이 나머지 부분집합과 내가만든 부분집합과 같으려면 토탈의 절반으로 같음(ex 12 면 6=6)
#sum이 토탈의 절반 넘어가면 바로 아닌게 되므로 이렇게 짜면 시간 복잡도를 줄일 수 있다.
#근데 꼭 이렇게 안될수도 11//2면 5인데  홀수 인경우 무조건 no만 나옴
#근데 홀수인데 yes 나올수도 13//2 =6 이 sum인데 왼쪽트리는 6인데 오른쪽트리는7
#아무튼 이렇게 sum이 total//2보다 크면 바로 리턴해서 종료

    if sum>total//2: #밑으로 뻗어나갈 필요가 없음.
        return
    if L==n:
        if sum==(total-sum): #(total-sum) 이 부분이 내가 만든 부분집합의 반대편임.
            print("YES")
            sys.exit(0) #yes 출력하고 바로 프로그램 종료(함수 종료가 아닌 프로그램 자체를 아예 종료)
    else:   #아니라면
        DFS(L+1, sum+a[L])
        #L은 인덱스번호(접근하는) a리스트의 L이 가리키고있는 그 값을 부분집합의 원소로 사용할거냐
        DFS(L+1, sum)


if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO") #프로그램 종료 안되고 여기로 오면 NO 출력