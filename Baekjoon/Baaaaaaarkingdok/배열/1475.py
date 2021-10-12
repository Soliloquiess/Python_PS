n = input()
a = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0} #이건 딕셔너리 써서 처음부터 0~8까지 0으로 초기화
for i in range(len(n)):
    if n[i] in ['6', '9']:
        a['6'] += 1
    else:
        a[n[i]] += 1
if a['6'] % 2 == 0:
    a['6'] = a['6'] // 2
else:
    a['6'] = a['6'] // 2 + 1
print(max(a.values()))
#https://pacific-ocean.tistory.com/97

# n = input() #다솜이 방번호를 string으로
# card=[0]*10 #0~9까지 번호
# card_6n9 = 0
#
# for i in n:
#     if(i=='6' or i=='9'): #6,9 동일취급
#         card_6n9 += 1
#     else:
#         card[int(i)] += 1
#
# #6, 9 개수 결정
# if(card_6n9 % 2 == 0):
#     card_6n9 = card_6n9//2
# else:
#     card_6n9 = card_6n9//2 + 1
#
# card[6] = card_6n9
#
# #card에 있는 것들 중 최대값이 세트의 개수
# print(max(card))


#n = int(input()) #다솜이 방번호
# card=[0]*9 #0~8까지 번호 (9는 따로)
# card_6n9 = 0
#
# while(n!=0):
#     a= n % 10
#     if(a==6 or a==9): #6이랑 9랑 같이 취급
#         card_6n9 += 1
#     else:
#         card[a] += 1
# #    n_arr.append(a)
#     n = n//10
#
# #n_arr.sort() #같은애들끼리 모음
#
# #01234578: 한 세트에 한 개
# #6 9 : 한 세트에 두 개 -> 올림
# if(card_6n9%2 == 0):
#     card_6n9 = card_6n9//2
# else:
#     card_6n9 = card_6n9//2 + 1
#
# set=max(max(card) , card_6n9)
# print(set)
# https://mminky.tistory.com/134