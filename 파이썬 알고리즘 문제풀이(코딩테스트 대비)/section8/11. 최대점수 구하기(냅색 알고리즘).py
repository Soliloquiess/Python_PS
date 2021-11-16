import sys
#sys.stdin = open("input.txt", 'r')

n, m=map(int, input().split())
dy=[0]*(m+1);#m까지 생긴다.

def solution(n,m):
    for i in range(n):    #행이 i고 열이 j
        ps, pt=map(int, input().split())

        for j in range(m, pt-1, -1):  #1씩 작아지면서 pt까지 돌음.

            dy[j]=max(dy[j], dy[j-pt]+ps) #j라는 값은 둘 중 큰값으로

            #dy[j-pt] 현재 주어진 시간 j라는 값에서 문제 푼다고 가정하므로 pt 뺴줌(그 시간만큼 뻄)
            #pt뺴는건 그 문제 푼다고 가정해서 빼주는 거
            #dy[j],  dy[j-pt]는 각 시간이 주어졌을때의 최대 점수


            #
            #dy[i-1][j-pt] 현재 적용되고 있는 타임 뺴준다
            #즉 dy[j]는 dy[j-pt] 시간이 주어졌을때의 최대 점수
            #dy[j]가 크면 그대로 두고 dy[j-pt]가 더 크면 바꿈.

    print(dy[m])# m분이 주어졌을 떄의 최대 점수
    return dy[m];
print(solution(n,m));
# if __name__=="__main__":
#     n, m=map(int, input().split())
#     dy=[0]*(m+1);#m까지 생긴다.
#
#
#     for i in range(n):    #행이 i고 열이 j
#         ps, pt=map(int, input().split())
#
#         for j in range(m, pt-1, -1):  #1씩 작아지면서 pt까지 돌음.
#             dy[j]=max(dy[j], dy[j-pt]+ps) #j라는 값은 둘 중 큰값으로
#             #dy[j-pt] 현재 주어진 시간 j라는 값에서 문제 푼다고 가정하므로 pt 뺴줌(그 시간만큼 뻄)
#             #pt뺴는건 그 문제 푼다고 가정해서 빼주는 거
#             #dy[j-pt]는 이 시간이 주어졌을때의 최대 점수
#
#
#             #
#             #dy[i-1][j-pt] 현재 적용되고 있는 타임 뺴준다
#             #즉 dy[j]는 dy[j-pt] 시간이 주어졌을때의 최대 점수
#             #dy[j]가 크면 그대로 두고 dy[j-pt]가 더 크면 바꿈.
#
#     print(dy[m])# m분이 주어졌을 떄의 최대 점수

#dy[i][j] = i번쨰까지 문제 적용함.
#dy[3][15]는 3번쨰 문제종류까지 적용하고 15분이 주어졌을 떄 최대 점수 기록한거.


#앞에서는 유사한 문제로 1차원

#근데 2차원 배열하면 메모리도 엄청 커지고 메모리도 커지면 시간복잡도도 안좋아 지므로
#실전에서는 1차원 배열로 많이 한다.