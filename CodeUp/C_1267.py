n = int(input())
# numbers = list(map(int, input().split()))
numbers = [];

for i in range(0, n):
    number =int(input());
    # number = list(map(int, input().split()))
    numbers.append(number);
sumOfNumber = 0

for number in numbers:
    if(number%5==0):
        sumOfNumber += number
print(sumOfNumber)