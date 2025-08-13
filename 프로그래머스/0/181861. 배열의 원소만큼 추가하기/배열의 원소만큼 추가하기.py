def solution(arr):
    answer = []
    for a in arr:
        answer += [a] * a  # a를 a번 반복해서 리스트에 추가
    return answer
