import sys
#sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    if L == n and sum == f: #n까지 가면 종료지점. sum도f까지 가면 종료(f 되면 답을 찾은거)
        for x in p: #p가 순열 저장하려고 만든거니까
            print(x, end=' ')   #답 출력
        sys.exit(0) #최초로 발견된거 하고 프로그램 종료(함수 종료가 아니라 프로그램 전체 종료)
    else:
        for i in range(1, n + 1):  #순열 만드는건 1부터 n까지
            #작은거부터 넣으면서 사전순으로 만들어감
            if ch[i] == 0: #ch[i]가 0이면 중복 방지
                ch[i] = 1  #ch[i]는 이제 사용했으니까 사용하지 말아라고 1 체크
                p[L] = i    #pl[l]에 i 넣는거 #순열 만드는 중
                DFS(L + 1, sum + (p[L] * b[L]))
                #레벨은 1 증가(순열 그대로 p[l] *b[l] . 근데 p[L] 대신 i써도 되긴 함 (같으므로)
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n     #여기에 순열 계속 만들어 나갈거
    b = [1] * n     #초기화 한거 해놓은거.(이항계수 여기 저장하는거)
    ch = [0] * (n + 1)  #순열 그대로 짜면 되는거
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i #초기화 및 누적현상
    DFS(0, 0)






