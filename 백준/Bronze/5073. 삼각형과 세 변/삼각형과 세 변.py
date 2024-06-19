while True:
    # 세 변의 길이를 입력받습니다.
    a, b, c = map(int, input().split())
    
    # 입력이 0 0 0인 경우 루프를 종료합니다.
    if a == 0 and b == 0 and c == 0:
        break
    
    # 삼각형이 유효한지 확인합니다.
    if a + b <= c or b + c <= a or c + a <= b:
        print("Invalid")
    # 세 변의 길이가 모두 같은 경우
    elif a == b and b == c:
        print("Equilateral")
    # 두 변의 길이만 같은 경우
    elif a == b or b == c or c == a:
        print("Isosceles")
    # 세 변의 길이가 모두 다른 경우
    else:
        print("Scalene")
