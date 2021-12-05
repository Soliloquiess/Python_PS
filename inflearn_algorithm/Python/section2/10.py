import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
cnt=0
sum=0
for i in range(n):
    if a[i]==1:     #1이면
        cnt=cnt+1      #cnt 값에+1하는데 거기에 cnt값은 연속이면 계속 늘어나니까 그 cnt값에 계속 더해지는거.(1,2,3,4...)
        sum=sum+cnt
    else:
        cnt=0       #만약 0 나오면 그 cnt도 0으로 만듬.

#for x in a:
#    if x==1:
#        cnt+=1;
#        sum +=cnt;
#    else:
#        cnt = 0;
print(sum)

# 1아니면 다시 0으로 돌아가고 그런게 아니라 전체 합산이다.