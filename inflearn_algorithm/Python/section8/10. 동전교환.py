import sys

#sys.stdin = open("input.txt", 'r')
#dy[j] : j원을 거슬러주는데 사용된 동전의 최소 개수.

n = int(input())
coin = list(map(int, input().split()))
m = int(input())

dy = [1000] * (m + 1);  # 다이나믹 테이블 만듬 M개 까지 하고 초기화는 1000으로
dy[0] = 0  # 0원 거슬러주는데 사용되는 동전의 개수는 0개

def solution(n,coin,m):
    for i in range(n):  # 0번부터 넣었으므로
        for j in range(coin[i], m + 1):  # 코인 i부터 돌아야 됨.
            dy[j] = min(dy[j], dy[j - coin[i]] + 1)  # 작으면 바꿔준다.
            # coin[i]이 코인 사용하겠다고 하고 뺸거 그리고 +1은 사용할 동전 한개 더하는거
    print(dy[m])
    return dy[m];
print(solution(n,coin,m));

# if __name__=="__main__":
#     n=int(input())
#     coin=list(map(int, input().split()))
#     m=int(input())
#
#
#     dy=[1000]*(m+1);  #다이나믹 테이블 만듬 M개 까지 하고 초기화는 1000으로
#     dy[0]=0           #0원 거슬러주는데 사용되는 동전의 개수는 0개
#
#
#     for i in range(n):#0번부터 넣었으므로
#         for j in range(coin[i], m+1): #코인 i부터 돌아야 됨.
#             dy[j]=min(dy[j], dy[j-coin[i]]+1) #작으면 바꿔준다.
#             #coin[i]이 코인 사용하겠다고 하고 뺸거 그리고 +1은 사용할 동전 한개 더하는거
#     print(dy[m])