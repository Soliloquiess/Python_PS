n = int(input())  # 입력값
num = 666  # num은 666
count = 0

while True:
    if "666" in str(num):  # num 문자열에 666이 있다면?
        count += 1  # count + 1
    if count == n:  # 더한 카운트와 입력값이 같다면 탈출
        print(num)  # num 출력
        break
    num += 1  # num에 666이 없다면 1을 더한다.

# https://velog.io/@kbhoon/%EB%B0%B1%EC%A4%80-1436-%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85-%EC%8A%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC