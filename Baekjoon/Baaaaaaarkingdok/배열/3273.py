import sys
input = sys.stdin.readline

n = int(input()) # 수열의 크기

li = list(map(int, input().split())) # 수열 입력
li.sort() # 오름차순 정렬

x = int(input()) # 목표값

cnt = 0 # 쌍의 갯수

left, right = 0, n-1

while left != right : # 왼쪽 인덱스와 오른쪽 인덱스가 같을 때까지 돌아라
    if li[left] + li[right] == x : # 왼쪽과 오른쪽의 합이 같으면 쌍 1개 증가하고, 왼쪽 인덱스 1 증가
        cnt += 1
        left += 1

    elif li[left] + li[right] > x :
        right -= 1

    else :
        left += 1

print (cnt)