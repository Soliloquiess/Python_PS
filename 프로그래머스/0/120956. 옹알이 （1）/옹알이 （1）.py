def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        temp = word
        used = set()  # 이미 사용한 발음 기록
        i = 0
        while i < len(temp):
            for s in sounds:
                if temp[i:i+len(s)] == s and s not in used:
                    used.add(s)
                    i += len(s)
                    break
            else:
                # 어떤 발음도 일치하지 않으면 불가
                break
        else:
            # 전체 순회 성공
            answer += 1

    return answer
