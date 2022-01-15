from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    # 유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:  # 유일성
            put = True

            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break

            if put: unique.append(i)

    return len(unique)


# from itertools import combinations
#
#
# def solution(relation):
#     # key의 개수
#     N = len(relation[0])
#     key_idx = list(range(N))
#     candidate_keys = []
#
#     for i in range(1, N + 1):
#         for comb in combinations(key_idx, i):
#             hist = []
#             for rel in relation:
#                 current_key = [rel[c] for c in comb]
#                 # 하나라도 중복되는 경우: 식별 불가능
#                 if current_key in hist:
#                     break
#                 else:
#                     hist.append(current_key)
#             # 하나도 중복 안 된 경우: 식별 가능
#             else:
#                 for ck in candidate_keys:
#                     # 최소성 확인
#                     if set(ck).issubset(set(comb)):
#                         break
#                 else:
#                     candidate_keys.append(comb)
#
#     return len(candidate_keys)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))