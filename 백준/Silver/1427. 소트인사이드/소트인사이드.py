N = int(input())
A = []
A = list(map(int, str(N)))
A.sort(reverse=True)
for n in A :
    print(n, end="")


#import sys

# 입력을 받습니다.
#input = sys.stdin.read().strip()
#N = input

# 숫자를 각 자리수별로 분리하고 정수로 변환 후 내림차순으로 정렬합니다.
#sorted_digits = sorted(N, reverse=True)

# 정렬된 리스트를 문자열로 합칩니다.
#result = ''.join(sorted_digits)

# 결과를 출력합니다.
#print(result)

# nums = input()
# nums = [int(n)  for n in nums]
#
# ordered_nums = sorted(nums, reverse=True)
#
# for n in ordered_nums :
#     print(n, end="")

# N = list(str(input()))
# N.sort(reverse = True)
# answer = ""
# 
# for i in N:
#     answer += i
# print(int(answer))

