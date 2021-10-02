import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()  #수열의 첫 자료값에 의해 정렬함.
    if len(tmp)==0: #종료조건.
        break;
    else:       #1개 아니면 2개 들어가서 정렬했을 거.
        res=res+tmp[0][1]   #0번은 제일 앞의 자료라는 거고 거기에 1번은 L이나 R. [0][0]은 a[lt]나 a[rt]가리킴
        #[0][1]은 그 뒤에 알파벳 가리킴.
        last=tmp[0][0]      #last는 숫자가 들어가야 됨
        if tmp[0][1]=='L':  #left인지 right인지 따라 숫자 움직여줘야 만약 L이면 Left에서 들감.
            lt=lt+1         #lt가 1 증가
        else:
            rt=rt-1         #rt는 1 감소(앞으로 전진해야 하므로)
    tmp.clear()             #tmp는 지워줘야.

print(len(res))             #수열의 길이 출력(문자열의 길이 == 수열의 길이)
print(res)                  #res라는 문자열 출력.