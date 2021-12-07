import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s = e =n//2  #일단 맨 첨에는 맨 위의 중간에서 시작해야 되므로.(s,e는 맨 첨에는 동일한 위치에 존재.)
for i in range(n):
    for j in range(s, e+1): #s부터 e까지 도는거(e+1이므로)
        res+=a[i][j] #맨 첨에는 a[2][2]더함.
    if i<n//2:  #i가 n//2보다 작으면 s,e 사이부분 길이가 늘어나는 거.
        s-=1 #여기서 1 뺴주는 거
        e+=1 #여기서 1 더해주는 거.
    else:       #i가 n//2보다 커지면 s,e 사이부분 길이가 줄어느는 거.
        s+=1
        e-=1
print(res)
