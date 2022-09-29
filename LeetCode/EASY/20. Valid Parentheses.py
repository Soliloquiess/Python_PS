class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
                continue
            if i == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] == '(':
                    stack.pop(-1)
                    continue
                else:
                    return False
            if i == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] == '{':
                    stack.pop(-1)
                    continue
                else:
                    return False
            if i == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] == '[':
                    stack.pop(-1)
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Solution()
    s = "{[}]"
    temp=a.isValid(s)
    print(temp);

# class Solution:
#     def isValid(self, s):
#         stack = []
#
#         for i in s:
#             if i in "([{":
#                 stack.append(i)
#             else:
#                 if not stack: #스택이 비었으면 false 리턴
#                     return False
#
#                 if i == "}" and stack[-1] != "{":
#                     return False
#
#                 if i == "}" and stack[-1] == "{":
#                     stack.pop()
#
#                 if i == "]" and stack[-1] != "[":
#                     return False
#
#                 if i == "]" and stack[-1] == "[":
#                     stack.pop()
#
#                 if i == ")" and stack[-1] != "(":
#                     return False
#
#                 if i == ")" and stack[-1] == "(":
#                     stack.pop()
#
#         return len(stack) == 0  # 0이면 True , 아니면 False
#
#
# if __name__ == "__main__":
#     a = Solution()
#     s = "()[]"
#     temp=a.isValid(s)
#     print(temp);

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#
#         # for i in s:
#
#         check = 0
#
#         for j in range(len(s)):
#             if s[j] == '(' or s[j] == '{' or s[j] == '[':
#                 check += 1
#             else:
#                 check -= 1
#
#             if check == -1:
#                         # answer = 'F'
#                 return False;
#                 break
#
#         for j in range(len(s)):
#             if check == 0 and s[len(s) - 1] == ')' and s[j] == '(':  # check가 0이고 마지막이 )이면 정상 괄호
#                 answer = True
#                 return answer
#
#
#             elif check == 0 and s[len(s) - 1] == '}' and s[j] == '{':  # check가 0이고 마지막이 )이면 정상 괄호
#                 answer = True
#                 return answer
#
#
#             elif check == 0 and s[len(s) - 1] == ']' and s[j] == '[':  # check가 0이고 마지막이 )이면 정상 괄호
#                 answer = True
#                 return answer
#             else:
#                 answer = False
#                 return answer
#
#
#
# if __name__ == "__main__":
#     a = Solution()
#     s = "()[]"
#     temp=a.isValid(s)
#     print(temp);


#이거 아래는 백준 9012 괄호 알파벳인지 뭔지 그거
#import sys

import sys

# T = int(sys.stdin.readline())
# T= int(input())
#
#
# for i in range(T):
#     D = input()
#     stack = []
#     for p in D:
#         if p == '(' or p =='{' or p =='[':
#             stack.append(p)
#         else:
#             for i in D:
#                 if len(stack) and p[i] == '(' and p[len-1] == ')':
#                     stack.pop()
#
#                 if len(stack) and p[i] == '{' and p[len - 1] == '}':
#                     stack.pop()
#
#                 if len(stack) and p[i] == '[' and p[len - 1] == ']':
#                     stack.pop()
#
#                 else:
#                     print('NO')
#                     break
#     else:
#         if stack:
#             print('NO')
#         else:
#             print('YES')


# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')