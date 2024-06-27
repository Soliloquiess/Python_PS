N = int(input().strip())

max_5kg_bags = N // 5

# 초기 결과를 -1로 설정합니다.
result = -1

# 5kg 봉지의 개수를 줄여가며 나머지를 3kg 봉지로 채울 수 있는지 확인합니다.
for i in range(max_5kg_bags, -1, -1):
    remaining_weight = N - (i * 5)
    if remaining_weight % 3 == 0:
        result = i + (remaining_weight // 3)
        break

# 결과를 출력합니다.
print(result)


# sugar = int(input())
#
# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)
