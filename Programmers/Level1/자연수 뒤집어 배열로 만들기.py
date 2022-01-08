# def solution(n):
#     arr = list(str(n))
#     arr.reverse()
#
#     return list(map(int, arr))
#
# print(solution(123))



def solution(n):
    a=[]

    while n>1:
        a.append(int(n%10))
        n/=10


    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.

print(solution(12345))



# class Solution {
# public int[] solution(long n) {
# String a = "" + n;
# int[] answer = new int[a.length()];
# int cnt=0;
#
#
# while (n > 0) {
# answer[cnt]=(int)(n % 10);
# n /= 10;
# cnt++;
# }
# return answer;
# }
# }