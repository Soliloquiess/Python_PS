import sys
# sys.stdin=open("input.txt", "r")
def Count(capacity):
    cnt = 1# 일단은 db 한장이 필요
    sum = 0
    for x in Music:
        # 노래에 시간 얼마나 있는가 저장한게 x값.
        if sum + x > capacity:
            # sum은 그 기존에 있던 곡들 저장(노래 시간 누적)
            # x 노래를 현재까지 저장된 용량에 합하는 거.
            # 이 x라는 곡도 현재 dvd더한 값에 저장할수 있는지.
            # 그 더한값이 용량보다 크면 새로운 dvd 필요
            # 기존에 저장하다가 새로운 노래를 저장한다 가정하고 기존용량보다 큰가봄.
            # x 노래를 현재까지 저장된 용량에다가  합해서 capacitiy보다 크면 x라는 곡은 현재 dvd에 저장 불가(요량초과)
            # 해서 새로운 dvd 필요해서 새롭게 x로 sum초기화( 처음 들어가는게 x라는 곡)
            # 그리고 dvd개수는 한개 늘림.

            cnt += 1  # dvd 한게 더함.
            sum = x  # 새로운dvd에 x값 저장해야 되므로 sum을 x값으로 초기화 함
            # sum에 새로운 노래 무조건 담는다
            # 넘어온 dvd용량은 어떤 노래보다도 크거나 같아야 함. .
        else:
            sum += x
            # sum에다 계속 누적.
    return cnt
    # 그걸 리턴해주면 됨.


# 반례는 9 9 들어오면 맨 마지막 9 들어가야되서 최소 디스크 크기는 9보다는 같거나 커야됨.
n, m = map(int, input().split())
Music = list(map(int, input().split()))

def solution(n,m,Music):
    maxx = max(Music)# 노래들 중 가장 큰 분을 같는 노래를 찾아줘야 그걸 maxx에 넣어줬다.
    lt = 1
    rt = sum(Music)
    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        if mid >= maxx and Count(mid) <= m:
            # Count(mid)<=m 이건 필요한 dvd개수가 넘어오면 m이하여야됨.
            # 2가 리턴되면 3장만에는 당연히 가능.


            # 반례를 수정하기 위해 mid>maxx라는 같을 넣어줘서
            # 가장 긴 노래보다는 dvd용량이 크거나 같아야 한다.
            # mid>=maxx 이 조건이 통과하면  count 함수 호출.

            res = mid  # 이 경우 답임.
            rt = mid - 1  # 그리고 더 좋은 답을 찾기위해 mid-1해서 탐색해줌.
        else:
            lt = mid + 1

    # print(res);
    return res;
print(solution(n,m,Music))