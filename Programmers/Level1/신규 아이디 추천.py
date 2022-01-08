def solution(new_id):
    answer = ""

    # 1 소문자 만들기
    new_id = new_id.lower()
    # 2 소문자, 숫자, 빼기, 밑줄, 마침표만 사용
    for value in new_id:
        if value.islower() or value.isdigit() or value in ["-", "_", "."]:
            answer += value

    # 3 . 두번 이상 반복되는 경우 .로 변경
    while '..' in answer:
        answer=answer.replace('..', '.')
        print(answer)

    # 4 .가 처음이나 끝에 위치하면 삭제
    if answer[0] == ".":
        if len(answer) >= 2:
            answer = answer[1:]
        else:
            answer="."

    if answer[-1] == ".":
        answer = answer[:-1]

    # 5 빈 문자열인 경우 a 대입
    if answer == "":
        answer = "a"
    # 6 16자리 이상인 경우 15자리까지 변경
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7 2자 이하인 경우 마지막 문자 추가
    while len(answer) < 3:
        answer += answer[-1]

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"));
# import re  # 정규 표현식을 사용하기 위한 re모듈 로드
#
#
# def solution(new_id):
#     # 1,2단계: 소문자, 숫자, -, _, . 을 제외한 나머지 제거 및 new_id 소문자화
#     a = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
#
#     # 3단계 : +는 앞문자 이상의 갯수 지정, 즉 .이 2개 이상인 문자열 .으로 치환
#     a = re.sub('\.\.+', '.', a)
#
#     # 4단계 : ^는 처음, $은 마지막, | or연산자 표현, 즉 처음 . 과 마지막 . 제거
#     a = re.sub('^\.|\.$', '', a)
#
#     # 5단계 : new_id가 비어있는 경우, 문자 a 추가
#     if a == "":
#         a = a + "a"
#
#     # 6단계 : a[:15] 범위 지정 및 마지막 . 제거(a[14]=='.' 방지)
#     a = re.sub('\.$', '', a[:15])
#
#     # 7단계
#     while len(a) <= 2:
#         a = a + a[len(a) - 1]
#
#     # 값 반환
#     return a