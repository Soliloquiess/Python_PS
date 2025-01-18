V = int(input())  # 심사위원 수 (사용 안함)
votes = input().strip()  # 투표 결과 문자열

count_A = votes.count('A')
count_B = votes.count('B')

if count_A > count_B:
    print("A")
elif count_B > count_A:
    print("B")
else:
    print("Tie")
