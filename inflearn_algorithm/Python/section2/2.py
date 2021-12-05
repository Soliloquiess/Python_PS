import sys
#sys.stdin=open("input.txt", "r")
T=int(input())
for t in range(T): #t는 0부터 테스트 케이스 만큼 돈다
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))

    a=a[s-1:e]  #첫번째꺼가 0번이므로 -1해줘야 e도 마찬가지로 e-1까지이므로

    a.sort()
    print("#%d %d" %(t+1, a[k-1]))