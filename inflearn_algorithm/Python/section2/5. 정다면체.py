import sys

#sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
ans = []
# ans = {}

global max; # 이거 global 쓰려면 선언 한 다음에 대입해야 한다. 이런 18
max = -2147000000  # 최대값은 가장 작은값으로.

def solution(n,m,max):  #
    cnt = [0] * (n + m + 3)
    #cnt 리스트 하나 만듬. 0으로 초기화 하고 크기는 n+m 이 숫자 이상은 안나옴.
    #cnt가 이 크기 ((n + m + 3)) 만큼 개수 생김.(눈의 합이 n+m) +3은 그냥 넉넉하게 잡기위해 붙여줌.,

    # global max;  # 이거 global 쓰려면 선언 한 다음에 대입해야 한다. 이런 18
    # max = -2147000000  # 최대값은 가장 작은값으로.

    for i in range(1, n + 1): #1부터 n까지 돔.
        for j in range(1, m + 1): #1이 또 나올수 있으므로(주사위니까) 이러면 6*4 다 돌수 있다.
            cnt[i + j] = cnt[i + j] + 1 #i+j가 눈의 합. 그리고 이 곳을 증가시켜줘야 됨..
    #1 2 3 4 5 6 7 .. xx 쭉 가면서 해당 인덱스면 +1하는거. 그럼 해당 수가 몇번 등장하는지 다 알고

    for i in range(n + m + 1): # cnt리스트에서 빈도회수의 최대값 찾음. n+m+1까지 해야 n+m까지 돔.
        if cnt[i] > max:       #max보다 크면 cnt[i]로 바꿔줘야 됨.
            max = cnt[i]       #

    for i in range(n + m + 1): #출력하는거
        if cnt[i] == max:  #최대값이 같은거 인덱스 다 출력
            # print(i, end=' ')
            ans.append(i);  #리스트로 하면 append(i)쓰면 된다.
            # ans.setdefault(i) #딕셔너리 {} 사용시 setdefault 사용해야 i 가 딕셔너리로 설정한 ans에 들어가게 된다. 대신 키만 들어가고 값이 없어서
            #{5: None, 6: None, 7:None} 이런식으로 나오게 된다.
    return ans;

print(solution(n,m,max));
