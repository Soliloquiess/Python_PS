def solution(arr):
    result = []  # 빈 리스트 생성
    for char in arr:
        result.append(char)  # 리스트에 문자 추가
    
    return ''.join(result)  # 리스트의 요소들을 문자열로 변환