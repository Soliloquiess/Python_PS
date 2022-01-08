def solution(n):
    nList = list(map(int, str(n)));
    newL = sorted(nList, reverse=True);
    strings = [str(i) for i in newL];
    a_string = "".join(strings)

    return int(a_string);

print(solution(118372))

# -> sorted 사용 : 새로운 정렬된 리스트를 반환하기 때문. list.sort() 메서드를 사용하면 리스트를 제자리에서 수정. None을 반환(원래 목록이 필요한 경우 이러면 사용할 수 없음.)
# -> list.sort()와 sorted()는 모두 불리언 값을 갖는 reverse 매개 변수를 받아들임.

# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))