a = int(input())
b = input()
for i in range(2, -1, -1):
    print(a * int(b[i]))
print(a*int(b))

----
# (1) 위치의 세 자리 수 입력
num1 = int(input())

# (2) 위치의 세 자리 수 입력
num2 = int(input())

# (3) 위치에 들어갈 값을 계산
val3 = num1 * (num2 % 10)

# (4) 위치에 들어갈 값을 계산
val4 = num1 * ((num2 // 10) % 10)

# (5) 위치에 들어갈 값을 계산
val5 = num1 * (num2 // 100)

# (6) 위치에 들어갈 값을 계산
val6 = num1 * num2

print(val3)
print(val4)
print(val5)
print(val6)
