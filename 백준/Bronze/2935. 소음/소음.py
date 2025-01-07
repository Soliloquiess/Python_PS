A = input().strip()
operator = input().strip()
B = input().strip()

if operator == '+':
    result = int(A) + int(B)
elif operator == '*':
    result = int(A) * int(B)

print(result)
