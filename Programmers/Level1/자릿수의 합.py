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



# ================
#
# 파이썬만의 방법
#
#
# import sys
# #sys.stdin=open("input.txt", "r")
# def digit_sum(x):
#     sum=0
#     #넘어온 정수를 바로 스트링 처리해서 할 수도(파이썬이라 문자열로 가능)
#     #i가 하나하나 문자열 접근
#     for i in str(x):
#         #print(i,end = ' ')
#         sum +=int(i);
#     return sum;
#     #print();
#
# n=int(input())
# a=list(map(int, input().split()))
# res=0
#
# #max=-2147000000
# max=float('-inf')
# for x in a:
#     tot=digit_sum(x)
#     if tot>max:
#         max=tot
#         res=x
# print(res)