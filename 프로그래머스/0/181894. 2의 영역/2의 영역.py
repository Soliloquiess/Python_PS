def solution(arr):
    first = -1
    last = -1

    # 직접 루프를 돌면서 2의 위치 추적
    for i in range(len(arr)):
        if arr[i] == 2:
            if first == -1:
                first = i
            last = i

    # 2가 없으면 [-1] 반환
    if first == -1:
        return [-1]
    
    # 슬라이싱으로 결과 리턴
    return arr[first:last+1]


#def solution(arr):
#    if 2 not in arr:
#        return [-1]
    
#    first = arr.index(2)             # 첫 번째 2의 위치
#    last = len(arr) - 1 - arr[::-1].index(2)  # 마지막 2의 위치
    
#    return arr[first:last+1]
