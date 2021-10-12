testcase = int(input())

for _ in range(testcase):
    press_key = input()
    cursor_left, cursor_right = [], []
    for word in press_key:  #press_key 넣은거에 word가 있는 동안
        if word == '-':
            if cursor_left: #cursor_left에 든게 있으면 참이라 실행
                cursor_left.pop()
        elif word == '<':
            if cursor_left: #cursor_left에 든게 있으면 참이라 실행
                cursor_right.append(cursor_left.pop())
        elif word == '>':
            if cursor_right:    #cursor_right에 든게 있으면 참이라 실행
                cursor_left.append(cursor_right.pop())
        else:
            cursor_left.append(word)    #cursor_left에 든게 있으면 참이라 실행

    while cursor_right:  #cursor_right에 든게 있으면 참이라 실행
        cursor_left.append(cursor_right.pop())  #cursor_right에 있는 걸 cursor_left에 다 넣어준다.(옮겨서)
    print(''.join(cursor_left))

#https://codingcocoon.tistory.com/139