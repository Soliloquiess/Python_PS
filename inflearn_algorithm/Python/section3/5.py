import sys
#sys.stdin = open("input.txt", 'r')
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0 #인덱스 0을 가리키는 거.
rt=1 #인덱스 1을 가리키는 거.(인덱스 0의 바로 오른쪽 가리킴)
tot=a[0] #tot는 a[0]으로 해두면 1이고(lt부터 rt바로 전 자료 까지의 연속부분의 합)
cnt=0

#무조건 lt는 rt보다 작거나 같아야.
#rt가 n인 상황에서 또 +1인 상황오면 그 때 break하는거
#lt랑 rt가 같아질수 는 있는데 lt가 더 커질 수는 없음(rt전까지의 합인데 그럼 0이므로)
#lt와 rt가 같으면 무조건 0(rt 전 까지의 합이므로)
#tot값이 m보다 작으면  lt한칸 올리고 m보다 크면 rt 한칸 올리고
#마지막은 rt가 8가리키고 lt가 6가리키고 3만듬
#rt가 n까지 오면(rt가 커져야 되는데 n-1까지 다 처리하고 n까지 왔는데 거기서 더 증가시키면 break;)

while True:
    if tot<m:
        if rt<n: #n보다 작을 때 까지만
            tot+=a[rt]
            rt+=1
        else:   #tot가 m보다 작은데 rt가 n에 가 있는 경우임.
            break
    elif tot==m:    #같으면
        # (여기서 단일항목이 바로 m인경우 lt==rt로 바로 답이 나와서 cnt+1이 될 수 도 있다.)
        cnt+=1 #카운트
        tot-=a[lt]  #lt가 가리키는 값 빼주고
        lt+=1   #카운트 1 증가
    else:       #tot가 무조건 클 떄(작던지 같던지가 아니면 무조건 크니까)
        tot-=a[lt]
        lt+=1
print(cnt)