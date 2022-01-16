# def solution(k, dungeons):
#     return search(k,dungeons,0)
#
# def search(k,list_d,count):
#     #print('피로도 : {} 탐색한 던전 수: {}  남은 던전: {}'.format(k,count,list_d))
#     count_list=[count]
#     for i in range(len(list_d)):
#         if list_d[i][0]<=k:
#             tmp_list=list_d.copy()
#             del tmp_list[i]
#             count_list.append(search(k-list_d[i][1],tmp_list,count+1))
#     #        if count==0:
#     #            print('----------------------------------------------')
#     return max(count_list)
#dfs 버전
#
# https://lyeong-gwa.tistory.com/32

from itertools import permutations


def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0
    a =0;
    for permut in permutations(dungeons, dun_num):
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count

    return answer



print(solution(80,[[80,20],[50,40],[30,10]]	));