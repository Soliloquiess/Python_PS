import sys
#sys.stdin=open("input.txt", "r")

#이중포문은 시간복잡도 비효율적
#포문 하나로 가능
#키 정렬 내림차순하고 몸무게만 최대값을 구한다고 생각하고 카운트 하자.
#무조건 첫번째 사람은 카운팅.
#두번째 사람부터 쭉 몸무게가 최대값 될 수 있나 보는거.

n=int(input())
body=[]
for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))
body.sort(reverse=True) #키 순으로 정렬인데 내림차순으로 정렬.

largest=0;
cnt=0;
for x, y in body:
    if y>largest:   #몸무게 최대값 갱신 되는거
        largest=y   #y값으로 몸무게 최대값 변경
        cnt+=1      #카운트 +1;, 최대값이 갱신되는 시점에 그 사람은 선수 됨.
print(cnt)