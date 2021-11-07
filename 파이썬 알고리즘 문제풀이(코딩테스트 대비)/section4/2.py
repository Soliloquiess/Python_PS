import sys
#sys.stdin=open("input.txt", "r")
#
def Count(len): #길이 함수
    #len은 랜선 한개의 길이.
    cnt=0
    for x in Line:  #각각의 k개의 랜선이 하나하나 접근함.
        cnt+=(x//len) #k개의 랜선 하나하나 길이가 x인데 그걸 len으로 나눔.
        #예를들어 802//187 이렇게 나누면 4가 나오는데 이걸 저장하고 cnt에 넣음 그걸 누적
    return cnt #그 개수를 리턴해줌.

k, n=map(int, input().split())
Line=[] #list이름
res=0 #최대값(정답)
largest=0
for i in range(k):

    tmp=int(input()) #한개 숫자 읽는거
    #하나 읽어서 int화
    Line.append(tmp) #라인이라는 리스트에 추가.
    largest=max(largest, tmp) #하나하나 읽을때마다 largest찾으면 됨.
    #max라는 함수는 둘중 큰값을 구해줌.
    #기존값과 새로운 값중 큰 값을 largest에 넣어줌.
lt=1
rt=largest

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n: #Count함수 하나 생성.

        #그 개수가 n보다 크거나 같으면 답이 됨.
        res=mid     #답이 되면 res에 mid넣는거.
        lt=mid+1    #답이 되면 더 좋은 답이 있는지 확인하기 위해 mid+1을 해준다
    else:
        #답이 되지 않으면 답을 찾기위해 하나 줄임
        #긴쪽을 버리자.
        rt=mid-1
print(res)








