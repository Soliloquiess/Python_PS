import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
ans =[];
def reverse(x):
    res=0
    while x>0:              #32 -> 3
        t=x%10  #10으로 나눈 나머지 32 들어오면 여기선 2로 됨. 그 다음엔 t=3 되고
        res=(res*10)+t #숫자 뒤집는 과정.  사이클 1 = (0*10) +2  사이클2 = (2*10) + 3 = 23
        x=x//10 # 32에서 3으로 됨.  3/10의 몫은 0이되고 위 조건 실행 못하니까 리턴함.

        # remainder = number % 10
        # revs_number = (revs_number * 10) + remainder
        # number = number // 10

    return res

def isPrime(x):
    if x==1:
        return False                #1은 소수 아님. 그래서 FALSE 반환.
    # for i in range(2, x):           #x-1 까지 넣으면서 만약 x-1까지의 숫자중 나눠져서 0이 되면 소수가 아님.
    for i in range(2, x//2+1):        #(x // 2) + 1 까지 하면 소수 바로 찾을수 있다고 한다.(딱 중간까지만 계산 이러면 시간복잡도가 조금이라도 빨라질 듯.

        if x%i==0:
            return False
    return True

def solution(n,a):
    for x in a:
        tmp=reverse(x)
        if isPrime(tmp):    #여기서 False나오면 아래 print 문 실행 안하고 True일시 아래 print문 실행
            # print(tmp, end=' ')
            ans.append(tmp);
    return ans;
print(solution(n, a))