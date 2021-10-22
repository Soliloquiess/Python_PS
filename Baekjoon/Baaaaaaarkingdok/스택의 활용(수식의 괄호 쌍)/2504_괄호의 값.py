import sys

input = sys.stdin.readline

word = input()


# 1번. 완벽한 괄호인가 아닌가?
def isperfect(word):
    word_list = []
    for i in word:
        # 맨 처음에 닫힌 괄호가 나오면 False!
        if len(word_list) == 0 and (i == ']' or i == ')'):
            return False
        # 열린 괄호들은 무조건 넣어버리자. 대신 순.서.대.로
        elif i == '(' or i == '[':
            word_list.append(i)
        # 닫힌 괄호가 나오고 순서 리스트 끝이 같은 모양이면 없애버리기
        elif i == ')' and word_list[-1] == '(':
            word_list.pop()
        elif i == ']' and word_list[-1] == '[':
            word_list.pop()

    # 다했는데 남아있다? 대칭되지 않는다. 아마 남은건 열린 괄호일 것이다.
    if len(word_list) > 0:
        return False
    # 이걸 다했으면 완벽한 괄호가 된다.
    return True


# 2번. 완벽한 괄호 형식이니까 더하고 곱하고 해보자.
def calculate(word):
    sum_list = []
    for i in word:
        # 같은 방법으로 열린 괄호는 다 넣어주고
        if i == '(' or i == '[':
            sum_list.append(i)
        # 닫힌 괄호인데 마지막이 괄호이면 숫자를 넣어준다.
        elif i == ')' and sum_list[-1] == '(':
            sum_list.pop()
            sum_list.append(2)
        # 닫힌 괄호인데 리스트 마지막이 숫자이면 그 숫자이전을 확인하여
        # 열린 괄호를 찾을때까지 더해준다.(완벽한 형식이기 때문에 논리가 맞는다)
        elif i == ')' and sum_list[-1] > 0:
            part_sum = 0
            for j in range(len(sum_list) - 1, -1, -1):
                if type(sum_list[j]) == int:
                    part_sum += sum_list[j]
                    sum_list.pop()
                # 짝이 맞는 괄호를 만나면 반복을 종료한다.
                elif sum_list[j] == '(':
                    sum_list.pop()
                    break
            # 더한 숫자 값에 *2를 해 다시 넣어준다.
            sum_list.append(part_sum * 2)

        # 다른 괄호의 경우.
        elif i == ']' and sum_list[-1] == '[':
            sum_list.pop()
            sum_list.append(3)

        elif i == ']' and sum_list[-1] > 0:
            part_sum = 0
            for j in range(len(sum_list) - 1, -1, -1):
                if type(sum_list[j]) == int:
                    part_sum += sum_list[j]
                    sum_list.pop()
                elif sum_list[j] == '[':
                    sum_list.pop()
                    break
            sum_list.append(part_sum * 3)
    return sum_list


# 정의된 함수를 이용해 완벽한지 여부 파악 후, 더하기 함수로 반환했다.
if isperfect(word):
    print(sum(calculate(word)))
else:
    print(0)



# import sys
# # input = sys.stdin.readline
#
# s = input().rstrip()
#
# stackS = []
# stackB = []
# coeff = 1
# isPaired = True
# ans = 0
#
# for i in range(len(s)):
#     if s[i] == '(':
#         stackS.append(i)
#         coeff *= 2
#     elif s[i] == '[':
#         stackB.append(i)
#         coeff *= 3
#     elif s[i] == ')':
#         if stackS:
#             if s[i - 1] == '(':
#                 ans += coeff
#             stackS.pop()
#             coeff //= 2
#         else:
#             isPaired = False
#             break
#     elif s[i] == ']':
#         if stackB:
#             if s[i - 1] == '[':
#                 ans += coeff
#             stackB.pop()
#             coeff //= 3
#         else:
#             isPaired = False
#             break
# if not stackB and not stackS and isPaired:
#     print(ans)
# else:
#     print(0)