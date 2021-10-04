import sys
#sys.stdin=open("input.txt", "r")
a=list(range(21)) #0부터 20까지 숫자 생겨서 자동으로 리스트화
for _ in range(10):
    s, e=map(int, input().split()) #구간 읽는거
    for i in range((e-s+1)//2):     #+1을 해줘야 제대로 돔.(7-2)하면 5/2 하면 2인데 3번 돌아야 됨.근데 +1해주면 짝수던 홀수던 제대로 돔.
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0) #맨 앞 0은 사용하지 않았다. ㅇㅇ(0,1,2,3,4~20까지 배열이였음)
for x in a:
    print(x, end=' ')