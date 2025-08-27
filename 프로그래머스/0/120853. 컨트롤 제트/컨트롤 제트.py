def solution(s):
    stack = []
    for token in s.split():
        if token == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(token))
    return sum(stack)
