import sys
import math

limit = 123456
#문제에 123456 이하의 숫자가 입력 될 것이라고 했으므로, limit를 123456으로 설정했다.


eratos = [1] * (2 * limit + 1) #n부터 2n까지 계산을 해야하므로 limit의 2배 길이 리스트를 미리 생성하고 전부 1로 초기화했다.
#+1을 더해준 이유는 인덱스번호가 0부터 시작하기때문에 편의상 인덱스 번호와 실제 숫자를 맞춰주기 위함이다.
eratos[0] = 0
eratos[1] = 0
#0과 1은 소수가 아니므로 미리 0으로 체크해준다.


for i in range(2, int(math.sqrt(len(eratos)))):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(sum(eratos[n + 1:(2 * n) + 1]))   #미리 구해놓은 리스트에서 n보다 크고 2n보다 작거나 같은 소수의 갯수를 구해 출력한다.

# https://itholic.github.io/kata-bertrands-postulate/




