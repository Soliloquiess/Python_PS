import sys
def solution(n):
    sum=0
    while n>0:
        sum+=n%10       #sum에 x를 10으로 나눈 나머지 누적
        n=n//10         #x는 x를 10으로 나눈 몫으로 바뀜.
        #125 -> 12 ->1
        #sum = 5(125%10)+2(12%10)+1(1%10) = 8
    return sum;

print(solution(123));