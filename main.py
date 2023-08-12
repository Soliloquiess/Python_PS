def solution(strings, n):
    # n번째 문자를 추출하여 새로운 리스트에 저장
    nth_chars = [s[n] if len(s) > n else '' for s in strings]
    # strings와 nth_chars를 묶은 후, nth_chars를 기준으로 정렬
    sorted_strings = [s for _, s in sorted(zip(nth_chars, strings))]
    return sorted_strings


# # n번째 문자를 추출하여 새로운 리스트에 저장
# nth_chars = [s[n] if len(s) > n else '' for s in strings]
#
# # strings와 nth_chars를 묶은 후, nth_chars를 기준으로 정렬
# # zip() 함수를 이용하여 두 리스트를 묶은 후, nth_chars를 기준으로 정렬하고,
# # 두 리스트를 다시 unpacking하여 정렬된 strings를 얻는다.
# sorted_strings = [s for _, s in sorted(zip(nth_chars, strings))]
#
# # 정렬된 strings를 반환
# return sorted_strings
print(solution(["sun", "bed", "car"],2))

# https://school.programmers.co.kr/learn/courses/30/lessons/134240
