# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     #뒤에 나오는 if문의 조건을 만족하는 값(r)으로만 리스트를 구성한다는 의미
#     _lost = [l for l in lost if l not in reserve]
#
#     #reserve와 lost를 _reserve, _lost로 또 한 번 정의해 주는 이유는 뭔가
#     # =>서로 중복되어 있는 원소들을 빼고 리스트를 재정의 한것
#     for r in _reserve:  #이 _reserve안의 요소를 돌게 된다. 1,3,5였으면 1다음 3 다음 5가 오게 되는 것.
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)


# def solution(n, lost, reserve):
#     # 진짜 여유분이 있는 사람
#     real_reserve = [r for r in reserve if r not in lost]
#
#     # 진짜 잃어버린 사람
#     real_lost = [l for l in lost if l not in reserve]
#
#     # 여유분을 가지고 있는 사람
#     for i in real_reserve:
#         # 여유분 있는 사람의 앞
#         front = i - 1
#
#         # 여유분 있는 사람의 뒤
#         back = i + 1
#
#         # 여유분 있는 사람의 앞에 사람이 체육복이 없다면 나눠주고 값을 없애준다
#         if front in real_lost:
#             real_lost.remove(front)
#
#         # 여유분 있는 사람의 뒤가 사람이 체육복이 없다면 나눠주고 값을 없애준다
#         elif back in real_lost:
#             real_lost.remove(back)
#
#     return n - len(real_lost)

# def solution(n, lost, reserve):
#     reserve_n = list(set(reserve) - set(lost))
#     lost_n = list(set(lost) - set(reserve))
#
#     answer = n - len(lost_n)
#     for i in lost_n:
#         if i - 1 in reserve_n:
#             answer += 1
#             reserve_n.remove(i - 1)
#         elif i + 1 in reserve_n:
#             answer += 1
#             reserve_n.remove(i + 1)
#
#     return answer
# #https://kdgt-programmer.tistory.com/3


def solution(n, lost, reserve):
    set_reserve=set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
# https://rain-bow.tistory.com/30

print(solution(5,[2,4],[1,3,5]))

print(solution(5,[2,4],[3]))