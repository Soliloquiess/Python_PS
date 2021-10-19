def solution(sizes):
    sizes=[sorted(i) for i in sizes]    #아 여기서 정렬하는구나
    #이렇게 정렬하면 각 배열 안에서의 정렬이 됨 [60,50]->[50,60]이렇게
    maxWidth = [i[0] for i in sizes]
    maxLength = [i[1] for i in sizes]
    return max(maxWidth) * max(maxLength)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

# def solution(sizes):
#     answer1= max(max(x) for x in sizes);    #60,70,60,80(각 배열에서 큰 숫자들)
#     answer2= max(min(x) for x in sizes);    #50,30,30,40(각 배열에서 작은 숫자들)
#     ans=answer1*answer2;
#
# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
