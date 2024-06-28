import sys

# 빠른 입력을 위해 sys.stdin 사용
input = sys.stdin.read

# 입력값 처리
data = input().split()
N = int(data[0])
numbers = list(map(int, data[1:]))

# 오름차순 정렬
numbers.sort()

# 빠른 출력을 위해 sys.stdout 사용
sys.stdout.write('\n'.join(map(str, numbers)) + '\n')
