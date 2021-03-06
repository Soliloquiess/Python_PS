import sys

sys.stdin = open("input.txt", "r")


def DFS(L, s):  #섹션 5 에서 했던거 그대로( 조합 그대로 보여주면 됨.)
    global res
    if L == m:  #종착점에 옴.
        sum = 0 #도시의 피자거리
        for j in range(len(hs)):    #0부터 집의 개수만큼 돌아야 됨.
           
            #여긴 집의 좌표
            x1 = hs[j][0]           #0번이 튜플의 앞의 값
            y1 = hs[j][1]           #j번쨰 에. 1은 집의 튜플의 두번쨰 값
            dis = 2147000000        #각 집의 피자 배달거리 구하는데 그걸 dis로 해야.(최소값 구해야)
            for x in cb:    #cb에 저장 x가 pz의 인덱스 번호. 거기 좌표가 살아남은 피자집의 좌표가 됨.
                #x는 피자집 번호
                
                
                #여긴 피자집 좌표
                x2 = pz[x][0]       #pz의 x번쨰의 0번은  튜플의 첫번쨰 값
                y2 = pz[x][1]       #pz의 x번쨰의 0번은 튜플의 두번쨰 값
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
                #min(dis, abs(x1 - x2) 원래 dis값보다 작아야 됨.
                #abs(x1 - x2) + abs(y1-y2)이게 하나의 값.  이 값과 dis중 작은값이 dis로 갱신됨

            sum += dis              #포문 다 끝나면 dis에 제일 작은 값 저장됨.
            #그럼 sum에 누적하면 됨.(그리고 그게 도시 피자배달거리가 됨)
        if sum < res:       #sum이 res보다 작으면 res를 sum으로 바꿔주면 끝
            res = sum
    else:
        for i in range(s, len(pz)):#s부터 시작 , pz의 길이만큼 (6개니까 0~5까지 돈다)

            cb[L] = i   #이 s가 현재 가지가 큰거 받아야 한다.
            DFS(L + 1, i + 1)   #s엔 현재 가지 뻗은거에 +1을 해서 받음.


if __name__ == "__main__":
    n, m = map(int, input().split())    #n은 도시의 정보 격자의 크기, m은 살아남을 피자집 개수
    board = [list(map(int, input().split())) for _ in range(n)]
    #보드에 도시 지도정보 넣음
    hs = [] #하우스의 좌표정보
    pz = [] #피자집의 좌표정보
    cb = [0] * m    #컴비네이션의 약자 (m개 잡음) 피자집이 m개 살아남으니까
    # (조합의 경우수 저장)
    res = 2147000000    #

   #2중 포문 돌면서 집이면 hs, 피자집이면 pz에 넣음
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:    #집을 발견하면(1) 그 집의 좌표는 hs에 넣고
                hs.append((i, j))
            elif board[i][j] == 2:  #피자집을 발견하면(2) 그 피자집의 좌표는 pz에 넣음.
                pz.append((i, j))
    DFS(0, 0)
    print(res)


#집 정보 , 피자집 정보를 얻는다.
# 문제의 경우 2가 6개 즉 6개 중 4개를 뽑아내야한다.(입력 4개)
#6C4
#6개 중 4개를 뽑아내는 dfs