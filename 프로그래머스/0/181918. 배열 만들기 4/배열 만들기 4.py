def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if not stk:  # stk가 비어있으면
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:  # stk 마지막 원소가 arr[i]보다 작으면
            stk.append(arr[i])
            i += 1
        else:  # stk 마지막 원소가 arr[i]보다 크거나 같으면
            stk.pop()  # 마지막 원소 제거

    return stk
