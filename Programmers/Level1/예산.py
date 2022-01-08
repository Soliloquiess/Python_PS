def solution(d, budget):
    answer = 0
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        answer += 1

    return answer

# 각 부서마다 필요한 예산이 다 다르고, 최종 예산은 정해져있습니다.
# 이 문제의 목표는 최종 예산 내에서 최대한 많은 부서에게 지원을 하는 것입니다.
# 최대한 많은 부서에게 예산 지원을 하는 가장 쉬운 방법은 예산이 가장 적게 드는 부서부터 지원을 해주는 것입니다.
# 따라서 오름차순 정렬을 통하여 예산이 가장 적게 드는 부서부터 나열하고, 총 예산에서 예산이 동날 때까지 차례대로 빼주면 됩니다.

print(solution([1, 3, 2, 5, 4],9))