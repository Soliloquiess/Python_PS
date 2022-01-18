
# def solution(n, words):
#     answer = [0, 0]
#     count = 1 # range가 1부터 시작하므로, 1으로 설정
#     for idx in range(1, len(words)): # 1부터 시작하는 이유는 첫번째 사람의 첫 단어는 절대 틀릴 일이 없음
#         word = words[idx] # words[idx] : 언급된 단어
#         count %= n
#         if (word in words[0:idx]) or (words[idx-1][-1] != word[0]):
#             answer = [count +1, 1 + idx//n]
#             return answer
#         count +=1
#     return answer


def solution(n, words):
    answer = [0, 0]

    cnt = 0  # 탈락번호,차례 계산할 변수
    checks = []  # 나온 단어 확인할 리스트
    checks.append(words[0])
    for i in range(1, len(words)):  # 단어 순회하면서
        cnt += 1
        # 아직 안나온 단어이면서 & 앞 단어의 마지막 알파벳과 일치하면 checks 리스트에 넣음 (pass)
        if words[i] not in checks and list(words[i - 1])[-1] == list(words[i])[0]:
            checks.append(words[i])
        else:  # (fail)
            answer[0] = cnt % n + 1  # 탈락번호
            answer[1] = cnt // n + 1  # 탈락차례
            break

    return answer


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	));
