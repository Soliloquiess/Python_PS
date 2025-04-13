def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        possible_values = [x for x in arr[s:e+1] if x > k]
        
        if possible_values:
            answer.append(min(possible_values)) 
        else:
            answer.append(-1) 
    
    return answer


# def solution(arr, queries):
#     answer = []
#     for s, e, k in queries:
#         possible_values = []
#         for i in range(s, e + 1):
#             if arr[i] > k:
#                 possible_values.append(arr[i]) 
        
#         if possible_values:
#             answer.append(min(possible_values))  
#         else:
#             answer.append(-1) 
    
#     return answer
