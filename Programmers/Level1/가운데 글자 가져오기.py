def solution(s):
    answer = ''

    word_len = len(s)//2;
    if(len(s) % 2==0):
        answer= s[word_len-1:word_len+1];
    else:
        answer=s[word_len]

    return answer

print(solution("abc1de"))

# def solution(s):
#     #홀수
#     if len(s)%2 == 1:
#         return s[len(s)//2]
#     #짝수
#     else :
#         return s[(len(s)//2)-1:(len(s)//2)+1]
# print(solution("abc1de"))
