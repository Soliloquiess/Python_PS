import sys

#sys.stdin = open("input.txt", 'r')
n = int(input())
def solution(n):
    dy = [0] * (n + 1)  #1차원 배열(리스트) 파이썬에서 배열은 리스트니까
    dy[1] = 1
    dy[2] = 2
    for i in range(3, n + 1):
        dy[i] = dy[i - 1] + dy[i - 2]

    print(dy[n])
    return dy[n];
print(solution(n));


#동적 계획법(dp) = 점화식 사용