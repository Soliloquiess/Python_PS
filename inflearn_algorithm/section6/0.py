#재귀함수와 스택
import sys
def DFS(x):
    if x>0:
        #print(x)
        DFS(x-1)
        print(x)

if __name__ =="__main__":
    #main 선언하면 여기부터 실행
    n=  int(input());
    DFS(n);