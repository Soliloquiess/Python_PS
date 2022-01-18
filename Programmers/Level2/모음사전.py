# # 블로그 참고 코드
# def solution(word):
#     char = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
#     answer = len(word) # A를 0으로 두었기 때문에 길이로 초기화 필요
#     re = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1 # 781
#     for i in word:
#         answer += re * char[i] # 첫 문자가 무슨 글자로 시작하는지
#         re = (re - 1) // 5
#     return answer


def solution(word):
    answer = 0
    word_dic = {"E": 1, "I": 2, "O": 3, "U": 4}

    for i in range(len(word)):
        if word[i] == "A":
            answer += 1
        else:
            for j in range(4, i, -1):
                answer += (5 ** (j - i)) * word_dic[word[i]]
            answer += word_dic[word[i]] + 1

    return answer

print(solution("AAAAE"));
print(solution("AAE"));
