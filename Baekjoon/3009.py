x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)


for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)

#브3이였는데 헷갈렸다. x_nums[i]에서 5의 개수, 7의 개수가 각 2,1이였고 [5, 5, 7]
                    # y_nums[i]에서 5의개수, 7의개수가 각 1,2였음. [5, 7, 5]
                    # 그래서 1이 아닌 거 중 7 7 이 둘다 1이여서 7,7이 답인거.