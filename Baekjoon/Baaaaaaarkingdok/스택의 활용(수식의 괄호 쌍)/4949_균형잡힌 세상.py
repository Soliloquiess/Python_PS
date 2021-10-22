while True:
    s = input()
    if s == '.':
        break
    str = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            str.append(i)
        elif i == ')':
            if not str or str[-1] == '[':
                temp = False
                break
            elif str[-1] == '(':
                str.pop()
        elif i == ']':
            if not str or str[-1] == '(':
                temp = False
                break
            elif str[-1] == '[':
                str.pop()
    if temp == True and not str:
        print('yes')
    else:
        print('no')