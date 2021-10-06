import sys
import itertools as it  #이게 순열이나 조합 자동으로 구해줌.
#sys.stdin=open("input.txt", "rt")

#09번 수열 추측하기를 파이썬 라이브러리로 풀어보는거

n, f=map(int, input().split())
b=[1]*n #b가 1로 초기화
cnt=0
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i     #이 부분이 뒤에 다 초기화(앞에서 했던 것들)
a=list(range(1, n+1))       #1부터 n까지 리스트 초기화    (n이 4라면 1부터 4까지 초기화 됨)
for tmp in it.permutations(a):  #순열 구하는 부분.
    #it로 순열 씀. 그리고 permutations하고 안에 (a)넣으면 a에 있는 자료를 모든 순열의 경우 다 구해줌.
    #print(tmp); #이부분 실행해보면 1,2,3,4로 구할수 있는 모든 순열의 경우 출력해줌.
    #만약 순열중 3개만 뽑고싶다? 그럼 a 뒤에 숫자 붙이면 됨
    # 예)for tmp in it.permutations(a,3):
    #근데 코테에서 저 라이브러리 막을수 도 있음. 그러니까 라이브러리 없는 버전으로 연습하는게 더 좋을수도.

    sum=0
    for L, x in enumerate(tmp): #이럼 모든 경우들 다 출력.
        sum+=(x*b[L])
    if sum==f:                  #sum이 f인지 확인해서 답 맞으면 순열 출력.
        for x in tmp:
            print(x, end=' ')
        break

# b와 tmp 값 곱해줘야 x*b[L] 이렇게 곱해서 sum에 누적해야.



# for L, x in enumerate(tmp): #이럼 모든 경우들 다 출력.
#     sum+=(x*b[L])
#
# 이거 했으면
#
# 0 1
# 1 2
# 2 3
# 3 4
# 이렇게 나올건데 앞 숫자가 인덱스, 뒤 숫자가 들어간 숫자 번호다.

#b라는 곳에 1 3 3 1이 있고 tmp에 1 2 3 4면 도는게 x값이고 곱해준다음
# sum에 더해줘야
#x * b[L]하고 sum에 누적하기 위해 enumerate로 sum에 접근
# sum +=(x*b[L]);
#만약 답이면

#참고로 라이브러리에 너무 의존하지 말자 ㅇㅇ(라이브러리 없는 코테일 수도 있다.)