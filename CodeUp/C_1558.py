num=int(input())

def f(n):
    r=0;
    while(int(n)!=0):
        r= int(r*10)
        r= r + int(n%10);
        n = int(n//10);
    return r;
print(f(num));

# # Ask for enter the number from the use
# number = int(input("Enter the integer number: "))
#
# # Initiate value to null
# revs_number = 0
#
# # reverse the integer number using the while loop
#
# while (number > 0):
#     # Logic
#     remainder = number % 10
#     revs_number = (revs_number * 10) + remainder
#     number = number // 10
#
# # Display the result
# print("The reverse number is : {}".format(revs_number))

# number=input()
#
# def f(number):
#     number=list(number)
#     number.reverse()
#     print(''.join(number))
# f(number)


# n = list(map(int,str(input())))
# n.reverse()
# m = ""
# for i in n:
#     m += str(i)
# print(m)