import sys
N = 10001
sieve = [True] * N
def prime_sieve(N): #여기서 모든 소수 아닌 수 들 다 False로 만듬.
    for i in range(2, N):
        if sieve[i]:
            for j in range(2*i, N, i):
                sieve[j] = False
prime_sieve(N)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    idx = 0
    while True:
        if sieve[n//2 - idx] and sieve[n//2 + idx]: #둘 다 참일 때
            print(n//2 - idx, n//2 + idx) #출력하고 break 한다음 다음 입력으로 넘어간다.
            break
        idx += 1

#https://wlstyql.tistory.com/76?category=852442


# 소수 집합 만들기
# nums = {x for x in range(2, 10_001) if x == 2 or x % 2 == 1}
# # nums = 2와 홀수로 이루어진 집합
# for odd in range(3, 101, 2): # 101 == int(math.sqrt(10_000)) + 1
#     nums -= {i for i in range(2 * odd, 10_001, odd) if i in nums}
#     # 홀수의 배수로 이루어진 집합을 빼줌
#
# # 골드바흐 수를 출력
# t = int(input())
# for _ in range(t):
#     even = int(input())
#     half = even//2  # 입력받은 짝수를 2로 나눈 몫을 구함. / 기호를 쓰면 실수가 됨.
#     for x in range(half, 1, -1):  # 차이가 적은 두 수를 구하기 위해서 큰수부터 꺼냄
#         if (even-x in nums) and (x in nums):  # even-x 와 x가 소수 집합에 포함 되었는지 확인
#             print(x, even-x)  # 작은수부터 출력
#             break


#https://ooyoung.tistory.com/100