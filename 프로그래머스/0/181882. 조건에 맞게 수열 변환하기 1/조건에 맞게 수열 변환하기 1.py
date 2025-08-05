def solution(arr):
    result = [] 

    i = 0
    while i < len(arr):
        n = arr[i]

        if n >= 50 and n % 2 == 0:
            result.append(n // 2)
        elif n < 50 and n % 2 == 1:
            result.append(n * 2)
        else:
            result.append(n)
        
        i = i + 1
    
    return result


#def solution(arr):
#    result = []

#   for n in arr:
#        if n >= 50 and n % 2 == 0:
#            result.append(n // 2)
#       elif n < 50 and n % 2 == 1:
#            result.append(n * 2)
#        else:
#            result.append(n)  
#    return result

