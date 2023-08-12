def find_even_number(n, m) :
    numbers = [i for i in range(n, m + 1)]
    count = (m + 1 - n)/2
    if count == 0 :
        for the_num in numbers :
            if the_num % 2 == 0 :
                print(f'{the_num} 짝수')
    else :
        for the_num in numbers :
            if the_num % 2 == 0 :
                print(f'{the_num} 짝수')
                if (count + 1) > the_num > (count - 1) :
                    print(f'{the_num} 중앙값')

n = int(input('첫 번째 수 입력: '))
m = int(input('두 번쨰 수 입력: '))
find_even_number(n, m)