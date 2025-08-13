def solution(myStr):
    result = []
    current = ""

    for ch in myStr:
        if ch == 'a' or ch == 'b' or ch == 'c':  # 구분자일 경우
            if current != "":  # current가 비어있지 않으면 추가
                result.append(current)
            current = ""  # current 초기화
        else:
            current += ch  # 구분자가 아니면 current에 추가

    # 마지막 current 처리
    if current != "":
        result.append(current)

    # 결과가 비어있으면 ["EMPTY"] 반환
    if len(result) == 0:
        return ["EMPTY"]
    return result
