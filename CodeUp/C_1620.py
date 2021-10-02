n=int(input())

def sol(s):
    global n;   #전역변수 함수 안애서 쓰려면 global 추가해준다.
    s=0
    while(s==0 or s>=10): #두자리 수일 때만 돌기
        s: int=0
        while(n>0):
            s+=int(n%10)
            n = int(n/10)
        n=s
    return s;
print(sol(n))

# def solution(n):
#     if(n/10==0):
#         return n;
#     else:
#         return solution(n/10)+ solution(n%10);
#
# total =0;
# n= int(input());
#
# t = solution(n);
# while(t>=10):
#     t= solution(t);
# print(t);
#
# result = solution(int(input()));
#
# print(result);