# 테스트 케이스의 개수 T를 입력으로 받습니다.
T = int(input().strip())

# 각 테스트 케이스의 문자열을 입력받아 처리합니다.
for _ in range(T):
    string = input().strip()
    # 문자열의 첫 글자와 마지막 글자를 결합하여 출력합니다.
    print(string[0] + string[-1])
