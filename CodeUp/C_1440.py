n = int(input())
numbers = list(map(int, input().split()))

for i in range(0, n):
    number = numbers[i]
    if i == 0:
        number_list = numbers[1:]
    elif i == n-1:
        number_list = numbers[:-1]
    else:
        number_list = numbers[0:i] + numbers[i+1:]
    result = ' '

    for k in number_list:
        if number < k:
            result += '< '
        elif number > k:
            result += '> '
        elif number == k:
            result += '= '

    print(str(i+1) + ':' + result)