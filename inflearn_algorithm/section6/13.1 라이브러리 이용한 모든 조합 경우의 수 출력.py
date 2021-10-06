import sys
import itertools as it
# sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
for x in it.combinations(a, k):#a라는 리스트에서 k만 뽑아서 x에 대응
    #조합은 컴비네이션스 사용
    print(x);