import sys
#sys.stdin=open("input.txt", "r")
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10       #sum에 x를 10으로 나눈 나머지 누적
        x=x//10         #x는 x를 10으로 나눈 몫으로 바뀜.
        #125 -> 12 ->1
        #sum = 5(125%10)+2(12%10)+1(1%10) = 8
    return sum

n=int(input())
a=list(map(int, input().split())) #a라는 리스트 만들어서 저장.
res=0
max=-2147000000

#max=float('-inf') #숫자의 최소값.
for x in a:
    tot=digit_sum(x) #x라는 값의 자리수의 합.
    if tot>max:
        max=tot     #max는 tot로 바뀌고
        res=x       #tot를 만든 수 x가 들어감.
print(res)
