def f():
    max=li[0]
    cnt=0
    for i in range(a):
        if max<li[i]:
            max=li[i]
            cnt=i
    return cnt+1

a=int(input())
li=list(map(int,input().split()))
print(f())