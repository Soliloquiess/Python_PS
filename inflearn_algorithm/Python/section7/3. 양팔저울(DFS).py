import sys

#sys.stdin = open("input.txt", "r")
def DFS(L, sum):    #L은 각추의 인덱스 접근(1그램,3그램,7그램..))
    #sum은 특정할 수 있는 물의 무게
    # 왼쪽에 추를 넣으면 +, 오른쪽에 추를 넣으면 - 로 함.
    global res
    if L == n:  #n이 되었을 떄   종료지점
        if 0 < sum <= s:    #sum이 0보다 크고(양수여야하니까) s보다 작아야(총무게 = s)
            #음수는 안 봐도 됨.(강의 참조하면 더 좋긴 함)
            #마이너스가 있으면 분명 대칭구조에 양수가 생겨서 음수는 체크 안해도 됨.
            #그래서 중복 안시킬려고 set사용
            res.add(sum)    #
    else:
        DFS(L + 1, sum + G[L])  #다음추로 넘어가는거 L+1, sum에 G[L]을 왼쪽에 넣는거(+일때)
        DFS(L + 1, sum - G[L])  #다음추로 넘어가는거 L+1, sum에 G[L]을 오른쪽에 넣는거(+일때)
        DFS(L + 1, sum)         #이거는 현재 L번째 추를 무게 재는데 사용하지 않겠다는 뜻.
#여기서 +1, -1은 똑같이 추를 달지만 +1이 오른쪽에 그릇 추를 왼쪽 달아서 잰다고 가정하면
#-은 그 반대로 오른쪽에 추 왼쪽에 그릇 이런식
    return res;

if __name__ == "__main__":
    n = int(input())        #n에 추의 개수
    G = list(map(int, input().split())) #G라는 리스트에 각 추의 무게들 넣음
    s = sum(G)  #추 무게들의 총합
    res = set() #중복 제거하면서 값 넣기위해 set사용. 특정 될수있는 물의 무게들을 res에 추가
    print(DFS(0, 0))
    print(s - len(res)) #답출력(안 되는 경우의 수 출력이므로 les의 길이만큼 뺴줌)




