def solution(arr, flag):
    X = []

    for i in range(len(arr)):
        if flag[i]:
            # arr[i]를 arr[i]*2번 추가
            X += [arr[i]] * (arr[i] * 2)
        else:
            # 마지막 arr[i]개의 원소 제거
            X = X[:-arr[i]]

    return X



#def solution(arr, flag):
#    X = []

 #   for i in range(len(arr)):
#        if flag[i]:
            # arr[i]를 arr[i]*2번 반복해서 append
#            for _ in range(arr[i]*2):
#                X.append(arr[i])
 #       else:
            # 마지막 arr[i]개 제거
 #           for _ in range(arr[i]):
 #               X.pop()

  #  return X
