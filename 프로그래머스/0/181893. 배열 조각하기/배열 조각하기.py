def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:  # 짝수 인덱스 → 뒤 자르기 (query[i] 포함)
            arr = arr[:query[i]+1]
        else:  # 홀수 인덱스 → 앞 자르기 (query[i] 제외)
            arr = arr[query[i]:]
    return arr
