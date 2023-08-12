age=int(input('나이를 입력하세요: '))
cardcash=input('지불 방법을 입력하세요: ')
def pay(age, card):
    if age<8 or age>=75: return 0
    elif age<14: return 450
    elif age<20:
        if card=='카드': return 720
        else: return 1000
    else:
        if card=='카드': return 1200
        else: return 1300
print('나이: ',age, '세')
print('지불유형: ',cardcash)
print('버스요금: ',pay(age, cardcash),'원')