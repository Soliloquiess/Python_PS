n = int(input());
def solution(n):
    answer = 0;
    dy = [0] *31


    dy[1] = 1;
    dy[2] = 2;

    for i in range(3, n+1):
        dy[i] = dy[i - 2] + dy[i - 1];

    answer = dy[n];
    return answer;


print(solution(n))