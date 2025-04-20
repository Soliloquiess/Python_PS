def solution(l, r):
    from collections import deque
    
    result = []  # 결과를 저장할 리스트
    queue = deque(['5'])  # 큐에 시작 숫자 '5'를 넣음

    while queue:  # 큐가 비어있지 않으면 계속 반복
        num_str = queue.popleft()  # 큐에서 첫 번째 원소를 꺼냄
        num = int(num_str)  # 문자열을 정수로 변환

        if num > r:  # 만약 숫자가 r보다 크면 처리할 필요 없음
            continue
        if num >= l:  # 숫자가 l 이상이면 결과에 추가
            result.append(num)

        # 새로운 숫자들을 큐에 추가 (자릿수 늘리기)
        queue.append(num_str + '0')  # '0'을 추가한 새로운 숫자
        queue.append(num_str + '5')  # '5'를 추가한 새로운 숫자

    # 결과가 있으면 정렬해서 반환, 없으면 [-1] 반환
    return sorted(result) if result else [-1]


def solution(l, r):
    result = []  # 결과를 저장할 리스트
    queue = ['5']  # 큐에 시작 숫자 '5'를 넣음

    while queue:  # 큐가 비어있지 않으면 계속 반복
        num_str = queue.pop(0)  # 큐에서 첫 번째 원소를 꺼냄 (리스트의 경우 pop(0))
        num = int(num_str)  # 문자열을 정수로 변환

        if num > r:  # 만약 숫자가 r보다 크면 처리할 필요 없음
            continue
        if num >= l:  # 숫자가 l 이상이면 결과에 추가
            result.append(num)

        # 새로운 숫자들을 큐에 추가 (자릿수 늘리기)
        queue.append(num_str + '0')  # '0'을 추가한 새로운 숫자
        queue.append(num_str + '5')  # '5'를 추가한 새로운 숫자

    # 결과가 있으면 정렬해서 반환, 없으면 [-1] 반환
    return sorted(result) if result else [-1]
