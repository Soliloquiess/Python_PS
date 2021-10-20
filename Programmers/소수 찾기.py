import sys
def solution(n):
    #sys.stdin=open("input.txt", "r")
    # n=int(input())
    ch=[0]*(n+1) #0으로 초기화 되어야 그리고 n이 20이면 n+1 해야 0으로 20개 생김.
    cnt=0
    for i in range(2, n+1):
        if ch[i]==0: #cnt는 소수의 개수고 그 수(인덱스)가 1로 안되고 0으로 남아있으면 소수인거.
            cnt+=1
            for j in range(i, n+1, i):  #여기서 j가 또 돌음.
                #만약 j=2 aus 2의 배수로 반복하면서 1로 만듬(1로 변경하면서 체크하는거).
                #1로 체크하면 2의 배수니까 소수가 아니게 되는거이므로
                ch[j]=1    #만약 j의 배수이면 1로 다 초기화 한다.
    return cnt

#" k=2 부터 √N 이하까지 반복하여 자연수들 중 k를 제외한 k의 배수들을 제외시킨다"
#k = 2 이면 2 를 제외한 2의 배수를 모두 지워주고,
#k = 3 이면 3 을 제외한 3의 배수를 모두 지워주고,
#(4는 이미 k = 2 에서 제외되어 넘어간다.)
#k = 5 이면 5 를 제외한 5의 배수를 모두 지워주고..

#이렇게 하여 k = √N 까지 반복하는 방법이다
print(solution(20))