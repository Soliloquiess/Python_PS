def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if not s[i].isdigit():
                return False
        return True
    else:
        return False

print(solution("a123"))