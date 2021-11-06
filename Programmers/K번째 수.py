def solution(array,commands):
    answer=[]
    for i in commands:
        start,end,select=i  #이러면 [2,5,3] 이 i로 넘어오고 각 넘어온 값이 start에 들어가게 된다.
        b=array[start-1:end]
        b.sort()
        answer.append(b[select-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))