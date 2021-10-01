n = int(input())
dic = dict()

for i in range(n):
    name, score = map(str, input().split())
    dic[int(score)] = name

dic2 = sorted(dic.keys(), reverse=True)
# dic2 = sorted(dic.values(), reverse=True)
print(dic.get(dic2[2]))



######


# n = int(input())
# hash_record = {}
#
# for i in range(0, n):
#     name, score = input().split()
#     hash_record[name] = int(score)
#
# data = sorted(hash_record.items(), key=lambda t: t[1], reverse=True)
# print(data[2][0])
