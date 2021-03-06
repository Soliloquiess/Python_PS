import sys
#sys.stdin = open("input.txt", 'r')
#dy[j] = 가방의 j라는 무게까지 담을 수 있을 때 그떄 가방에 담을 수 있는 보석의 최대 가치.
#dy[j-w] = w는 빼는거는

if __name__=="__main__":
    n, m=map(int, input().split())  #n은 보석의 종류, m은 가방의 담을수 있는 무게

    dy=[0]*(m+1);#0으로 초기화 인덱스 번호 맞추기 위해 m+1

    for i in range(n):  #보석의 개수 만큼 돈다.
        w, v=map(int, input().split())  #하나씩 읽어줌.
        for j in range(w, m+1): #w부터 m+1까지 돌아야(j-w하니까 0부터 돌면 음수 인덱스 보게 됨.
            #현재 적용하고자 하는 보석의 무게부터 돌아야

            dy[j]=max(dy[j], dy[j-w]+v) #dy에 j라는 값은 기존 dy의 j값과 현재 보석 적용
            #현재 w무게와 v라는 가치를 갖는 보석을 담는 값 중 최대값
            #dy[j]는 기존에 있던 값.dy[j-w]는 w무게 보석 담는다 가정해서 그 무게만큼 빼둠
            #j-w는 그 무게만큼 담기위해 빈 공간 마련 거기에 v 보석 가치만큼 더해줌.
            #둘 중 더 좋은값으로 바꿔줌.
    print(dy[m])
