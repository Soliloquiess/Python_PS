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
