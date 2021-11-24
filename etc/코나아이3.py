check_numbers = [ "3285376499342453","328537649934245","3285376499352459"]

def Luhn_Check(number):
    """
        this function checks a number by using the Luhn algorithm.

        Notes (aka - How to Luhn) :
            Luhn algorithm works in a 1 2 1 2 ... order.
            Therefore, in computer speak, 1 0 1 0 ... order

            step 1:
                -> reverse the # so we are not working from right to left (unless you want too)
                -> double every second number

            step 2:
                -> if the doubled number is greater then 9, add the individual digits of the number to get a single digit number
                    (eg. 12, 1 + 2 = 3)

            step 3:
               -> sum all the digits, if the total modulo is equal to 0 (or ends in zero) then the number is valid...
    """

    reverse_numbers = [int(x) for x in number[::-1]] # convert args to int, reverse the numbers, put into a list
    dbl_digits = list() # create empty list
    digits = list(enumerate(reverse_numbers, start=1)) # enumerate numbers starting with an index of 1

    for index, digit in digits:
        if index % 2 == 0:  # double every second (other) digit.

            doub_digit = digit * 2
            dbl_digits.append(doub_digit - 9) if doub_digit > 9 else dbl_digits.append(doub_digit)

        else:
            # if not '0' append to list (this would be the 1 in Luhn algo sequence (1 2 1 2 ...)
            dbl_digits.append(digit)

    return sum(dbl_digits) % 10


if (__name__ == "__main__"):
    print("Valid Numbers: %s " % [x for x in check_numbers if Luhn_Check(x) == 0])


num = list(input("Please enter the number to test (no space, no symbols, only \
numbers): "))

num = list(map(int, num))[::-1] #let's transform string into int and reverse it

for index in range(1,len(num),2):
    if num[index]<5:
        num[index] = num[index] *2
    else: #doubling number>=5 will give a 2 digit number
        num[index] = ((num[index]*2)//10) + ((num[index]*2)%10)

checksum=sum(num)

print("checksum= {}".format(checksum))

if checksum%10 !=0:
    print('the number is not valid')
else:
    print('the number is valid!')

# card_num = ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453","328537649934245","3285376499352459","3285-3764-9934-2452"]
#
# List = []
# for card_num_index in card_num:
#     card_num_index = card_num_index.replace("-","")
#     List.append(card_num_index);
#
#
#
# a = list(range(0,len(List),2));
# print(a)
# List = []
# for i in range(0,len(card_num)):
#     List.append(card_num_index)
# # card_num_index = list(card_num_index)
# for i in range(0,len(card_num)):
#     print(List)
# for i in range(0,len(card_num)):
#     if(i//2==0):
#         print(card_num_index);



# [5, 3, 9, 13] 8 true
# [5, 3, 9, 13] 7 false
#
#
# card_num
# ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453","328537649934245","3285376499352459","3285-3764-9934-2452"]
#
