def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    #뒤에 나오는 if문의 조건을 만족하는 값(r)으로만 리스트를 구성한다는 의미
    _lost = [l for l in lost if l not in reserve]

    #reserve와 lost를 _reserve, _lost로 또 한 번 정의해 주는 이유는 뭔가
    # =>서로 중복되어 있는 원소들을 빼고 리스트를 재정의 한것
    for r in _reserve:  #이 _reserve안의 요소를 돌게 된다. 1,3,5였으면 1다음 3 다음 5가 오게 되는 것.
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)




print(solution(5,[2,4],[1,3,5]))

print(solution(5,[2,4],[3]))