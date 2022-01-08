def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s), i):
            if tmp == s[j:i + j]:   #뒤에꺼랑 같으면 cnt 추가
                cnt += 1
            else:
                if cnt != 1:    #cnt가 1이 아니면 중복되는(겹치는 문자)이므로 str(cnt)로 하나 늘려준다.
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j + i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp

        result.append(len(b))
    return min(result)

print(solution("aabbaccc"))
#https://eunhee-programming.tistory.com/135