x = int(input())
num_list = []
for i in range(x):  #len 안써야됨(int로 들어왔기 떄문)
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])