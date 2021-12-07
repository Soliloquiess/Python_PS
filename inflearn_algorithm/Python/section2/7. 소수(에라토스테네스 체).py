import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
def solution(n):
    ch=[0]*(n+1) #0으로 초기화 되어야 그리고 n이 20이면 n+1 해야 0으로 20개 생김.
    cnt=0
    for i in range(2, n+1):
        if ch[i]==0: #cnt는 소수의 개수고 그 수(인덱스)가 1로 안되고 0으로 남아있으면 소수인거.
            cnt+=1
            for j in range(i, n+1, i):  #여기서 j가 또 돌음.
                #만약 j=2 aus 2의 배수로 반복하면서 1로 만듬(1로 변경하면서 체크하는거).
                #1로 체크하면 2의 배수니까 소수가 아니게 되는거이므로
                ch[j]=1    #만약 j의 배수이면 1로 다 초기화 한다.
    # print(cnt)
    return cnt;
print(solution(n))

# 2에서 시작해서 배열 0인 부분일떄 카운트 1하고 전부 배열 1로 만들어서
# n+1까지 해서 끝나면 cnt 출력.