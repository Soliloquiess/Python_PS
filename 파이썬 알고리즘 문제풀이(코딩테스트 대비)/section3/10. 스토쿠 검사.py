import sys
#sys.stdin=open("input.txt", "r")
#행(ch1) 열(ch2) 그룹(ch3) 체크리스트 3개 필요
#체크리스트 합이 9가 아니면 잘못된거(스도쿠가 아님)
def check(a):
    for i in range(9):
        #0번인덱스는 사용 안할거긴함. 그래서 10개만듬
        ch1=[0]*10 #행을 가리키는 체크리스트
        ch2=[0]*10 #열을 가리키는 체크리스트
        for j in range(9): #0부터 8까지 돌면서 행과 열 탐색
            ch1[a[i][j]]=1 #j가 증가하므로 열이증가(가로로 증가) #0번 행을 탐색하는거
            ch2[a[j][i]]=1 #j가 증가하므로 행이증가(세로로 증가. #0번 열을 탐색하는거.
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False #둘중 하나만이라도 9가 아니면 return False
    for i in range(3):  #4중포문.. 선생님.. 이게 뭐..노..
        for j in range(3):
            #지금까지 2중포문은 3*3 을 다 0으로 초기화
            #여기는 9개의 그룹
            ch3=[0]*10

            for k in range(3):
                for s in range(3):
                    #여기는 9개의 숫자
                    #그리고 이부분은 위에 포문으로 0으로 3*3 배열 만들고  0으로 다 초기화
                    ch3[a[i*3+k][j*3+s]]=1
                    #i*3+k가 열(세로), j*3+s가 행(가로) 번호
                    #i*3이나 j*3은 계속 0
            if sum(ch3)!=9:
                return False
    return True #죽복이 없어서 정상종료

a=[list(map(int, input().split())) for _ in range(9)]
def solution(a):
    if check(a):
        # print("YES")
        return "YES";
    else:
        # print("NO")
        return "NO";

print(solution(a));