def solution(my_string, indices):
    result = ''
    for i in range(len(my_string)):
        if i not in indices:
            result += my_string[i]
    return result


# result = []
# for i, ch in enumerate(my_string):
#     if i not in indices_set:
#         result.append(ch)

# 이걸 한줄로 줄이면

# [ch for i, ch in enumerate(my_string) if i not in indices_set]


# def solution(my_string, indices):
#     # 삭제할 인덱스를 set으로 만들어 빠른 조회
#     indices_set = set(indices)
    
#     # 인덱스를 순회하며 삭제 대상이 아닌 문자만 남김
#     result = ''.join([ch for i, ch in enumerate(my_string) if i not in indices_set])
    
#     return result

# 문법 요소	의미
# enumerate(my_string)	인덱스와 문자 쌍 반복 ((i, ch))
# if i not in indices_set	해당 인덱스가 삭제 대상이 아니면
# ch	그 문자를 결과에 포함
# [...]	이렇게 모은 문자들을 리스트로 만듦
