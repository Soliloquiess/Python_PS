def solution(arr, queries):
    for query in queries:
        i, j = query
        arr[i], arr[j] = arr[j], arr[i]      
    return arr


# def solution(arr, queries):
#     for query in queries:
#         i, j = query[0], query[1]
        
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = temp
    
#     return arr
