a, b, c, d, e, f = map(int, input().split())

# (1) b * (첫 번째 방정식) - e * (두 번째 방정식) => y를 소거하기
det = a * e - b * d

if det != 0:
    x = (c * e - b * f) // det
    y = (a * f - c * d) // det

    print(x, y)
else:
    print("No unique solution")
