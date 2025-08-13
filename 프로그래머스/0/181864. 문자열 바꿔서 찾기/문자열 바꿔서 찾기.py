def solution(myString, pat):
    swapped = ""  # 바뀐 문자열을 저장할 변수

    # 한 글자씩 확인하며 A ↔ B 바꾸기
    for ch in myString:
        if ch == "A":
            swapped += "B"
        else:  # ch == "B"
            swapped += "A"

    # pat가 부분 문자열로 있는지 확인
    if pat in swapped:
        return 1
    else:
        return 0


#def solution(myString, pat):
    # "A" ↔ "B" 바꾸기
#    swapped = myString.replace("A", "C").replace("B", "A").replace("C", "B")
    
    # pat가 부분 문자열로 있는지 확인
#    if pat in swapped:
#        return 1
#    else:
#        return 0
