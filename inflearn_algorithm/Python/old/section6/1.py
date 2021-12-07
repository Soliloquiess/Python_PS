import sys
#sys.stdin=open("input.txt", "r")
def DFS(x):
    if x==0:
        return #아무 것도 없이 return 시 그냥 함수를 종료시킨다.
    else:
        #print(x%2, end='')
        DFS(x//2)   #x 를 2로 나눈걸 다시 매개변수로 넘김
        print(x%2, end='')

n=int(input())
DFS(n)
