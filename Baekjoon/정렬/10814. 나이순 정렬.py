# 10814번 : 나이순 정렬
n = int(input())

ls = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    ls.append((age, name))

# sort_ls = sorted(ls) -> A-Z 순으로 정렬되서 오답

ls.sort(key = lambda parameter_list: parameter_list[0])

"""
위 lambda식과 동일
ls안에 있는 것들이 parameter_list의 인수(argument)가 되어 
인덱스 [0]에 해당하는 age로만 정렬됨
인덱스 [1]로 하면 name으로 정렬할 것임
def ladmbda(parameter_list):
    return parameter_list[0]
"""

for i in ls:
    print(i[0], i[1])

# https://wook-2124.tistory.com/481
# https://dailyheumsi.tistory.com/67
# https://hyun-am-coding.tistory.com/entry/key%EC%99%80-lambda%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%A0%95%EB%A0%AC