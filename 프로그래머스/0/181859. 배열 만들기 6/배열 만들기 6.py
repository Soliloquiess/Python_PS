def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if not stk:  # stk이 비어있으면 arr[i] 추가
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:  # 마지막 원소와 같으면 제거
                stk.pop()
            else:  # 마지막 원소와 다르면 추가
                stk.append(arr[i])
        i += 1

    # stk이 비어있으면 [-1] 반환
    if not stk:
        return [-1]
    return stk
