import sys
#sys.stdin=open("input.txt", "r")
max=0
res=0
n=int(input())
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c=map(int, tmp) #매핑, a,b,c,가 숫자가 되서 매핑됨.
    if a==b and b==c:
        money=10000+(a*1000);
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money > res: #상금들 중 가장 큰 상금 찾는거.
        res=money

print(res)


