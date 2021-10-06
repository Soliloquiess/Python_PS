import sys
import itertools as it  #이게 순열이나 조합 자동으로 구해줌.
#sys.stdin=open("input.txt", "rt")

#09번 수열 추측하기를 파이썬 라이브러리로 풀어보는거

n, f=map(int, input().split())
b=[1]*n #b가 1로 초기화
cnt=0
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i     #이 부분이 뒤에 다 초기화(앞에서 했던 것들)
a=list(range(1, n+1))       #1부터 n까지 리스트 초기화    (n이 4라면 1부터 4까지 초기화 됨)
# print(a);

for tmp in it.permutations(a):
    print(tmp)


# for tmp in it.permutations(a,3): #만약 거기서 3개만 뽑아서 순열 만들라 하면 뒤에,3처럼 숫자를 붙여주면 된다.
#     print(tmp)