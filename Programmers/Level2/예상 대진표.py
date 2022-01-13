import math
def solution(n,a,b):
    answer = 0
    while a!= b:
        a = (a+1)//2
        b = (b+1)//2
        answer+=1
    return answer

def solution(n,a,b):
	answer = 0
	while a != b:
		answer += 1
        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 해서 나눴을때 몫이 1이 되도록
		a, b = (a+1)//2, (b+1)//2
	return answer


def solution(n,a,b):
    cnt=0
    while True:
        a= (a//2)+(a%
                   2)
        b= (b//2)+(b%2)
        cnt+=1
        if a==b:
            break
    return cnt
# 출처: https://eunhee-programming.tistory.com/145 [코드짜는 문과녀]
print(solution(8,4,7));
