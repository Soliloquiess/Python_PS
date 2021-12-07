import sys
#sys.stdin = open("input.txt", 'r')

#이 문제와 비슷하게 겹치는 선들중 최소 몇개를 제거해야 안 꼬이고 다리 이어지나 이런 문제도 있다(싸피)
#그러면 전체에서 최대부분 증가수열 lis구하고 뺴면 됨(ex) 10-6 =4 )
#컴퓨터 사고(컴띵)문제에서 이런 문제들 많이 나온다(싸피에서 이미 안겹치게 하는거 나왔잖아? 최대부분증가수열 이용(lis)

#오른쪽이 입력으로 주어진거. 여기서 최대부분증가수열 구함. 그리고 그 길이 출력
#앞 문제와 정확히 일치. 그대로 최대부분증가수열 구하고 그 길이 출력하면 됨.

#왼쪽에서 증가하는 수열이면 오른쪽에서도 증가하는 수열이여야한다.

#일단 선을 다 연결해두고 교차하는 선을 지우는 방법으로도 가능하다.

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
def solution(n,arr):
    dy=[0]*(n+1)
    dy[1]=1
    res=0

    for i in range(2, n+1):
        max=0
        for j in range(i-1, 0, -1):
            if arr[j]<arr[i] and dy[j]>max:
                max=dy[j]

        dy[i]=max+1
        if dy[i]>res:
            res=dy[i]

    print(res)
    return res;
print(solution(n,arr));