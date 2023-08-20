#6.1

korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

korea_names = korea_king.split(',')
chosun_names = chosun_king.split(',')

namesList = []

for name in korea_names:
    if name in chosun_names:
        namesList.append(name)
# namesList = [name for name in korea_names if name in chosun_names]
count = len(namesList)

print("중복되는 왕 이름 목록:")
for name in namesList:
    print(f"조선과 고려에 모두 있는 왕 이름 : {name}")

print(f"조선과 고려에 모두 있는 왕 이름은 총 {count}개 입니다")



# def find_duplicates(list1, list2):
#     return set(list1) & set(list2)
#
# korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
# chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"
#
# duplicate_names = find_duplicates(korea_king.split(','), chosun_king.split(','))
# duplicate_count = len(duplicate_names)
#
# print("중복되는 왕 이름 목록:")
# for name in duplicate_names:
#     print("조선과 고려에 모두 있는 왕 이름 :", name)
#
# print("조선과 고려에 모두 있는 왕 이름은 총 {}개 입니다".format(duplicate_count))


#6.2

def sales_management(member_names, member_records):
    # 멤버별 평균 실적 계산
    member_avg = []
    for records in member_records:
        avg = sum(records) / len(records)
        member_avg.append(avg)

    # 평균 실적을 기준으로 순위 계산
    rank = []
    for i in range(len(member_avg)):
        rank.append(i)
    rank.sort(key=lambda x: member_avg[x], reverse=True)

    # 보너스 대상자 선정
    bonus_members = []
    for i in range(2):
        if member_avg[rank[i]] > 5:
            bonus_members.append(member_names[rank[i]])

    # 면담 대상자 선정
    interview_members = []
    for i in range(4, 6):
        if member_avg[rank[i]] < 3:
            interview_members.append(member_names[rank[i]])

    # 결과 출력
    bonus_list = " ".join(bonus_members)
    interview_list = " ".join(interview_members)
    print(f"보너스 대상자 {bonus_list}")
    print(f"면담 대상자 {interview_list}")

# 주어진 데이터
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [
    [4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5],
    [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
    [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1],
    [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
    [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9],
    [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]
]

# 함수 호출하여 결과 출력
sales_management(member_names, member_records)

# def sales_management(member_names, member_records):
#     # 멤버별 평균 실적 계산
#     member_avg = [sum(records) / len(records) for records in member_records]
#
#     # 평균 실적 순위 계산
#     rank = sorted(range(len(member_avg)), key=lambda x: member_avg[x], reverse=True)
#
#     # 보너스 대상자 선정
#     bonus_members = []
#     for i in range(2):
#         if member_avg[rank[i]] > 5:
#             bonus_members.append(member_names[rank[i]])
#
#     # 면담 대상자 선정
#     interview_members = []
#     for i in range(4, 6):
#         if member_avg[rank[i]] < 3:
#             interview_members.append(member_names[rank[i]])
#
#     # 결과 출력
#     print("보너스 대상자", " ".join(bonus_members))
#     print("면담 대상자", " ".join(interview_members))
#
# # 주어진 데이터
# member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
# member_records = [
#     [4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5],
#     [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
#     [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1],
#     [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
#     [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9],
#     [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]
# ]
#
# # 함수 호출하여 결과 출력
# sales_management(member_names, member_records)



# def sales_management(member_names, member_records):
#     # 각 멤버의 평균 실적을 계산합니다.
#     member_avg_records = []
#     for records in member_records:
#         avg_record = sum(records) / len(records)
#         member_avg_records.append(avg_record)
#
#     # (이름, 평균 실적)으로 이루어진 튜플의 리스트를 생성합니다.
#     sorted_members = []
#     for name, avg_record in zip(member_names, member_avg_records):
#         sorted_members.append((name, avg_record))
#
#     # 평균 실적을 기준으로 내림차순으로 멤버를 정렬합니다.
#     sorted_members.sort(key=lambda x: x[1], reverse=True)
#
#     # 보너스 대상자를 결정합니다.
#     bonus_candidates = []
#     for name, avg_record in sorted_members[:2]:
#         if avg_record > 5:
#             bonus_candidates.append(name)
#
#     # 면담 대상자를 결정합니다.
#     counseling_candidates = []
#     for name, avg_record in sorted_members[4:]:
#         if avg_record <= 3:
#             counseling_candidates.append(name)
#
#     # 결과 출력
#     print("보너스 대상자", ', '.join(bonus_candidates))
#     print("면담 대상자", ', '.join(counseling_candidates))
#
#
# # 주어진 데이터
# member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
# member_records = [
#     [4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5],
#     [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
#     [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1],
#     [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
#     [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9],
#     [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]
# ]
#
# # 함수 호출하여 결과 출력
# sales_management(member_names, member_records)


# def sales_management(member_names, member_records):
#     # 각 멤버의 평균 실적을 계산합니다.
#     member_avg_records = []
#     for records in member_records:
#         avg_record = sum(records) / len(records)
#         member_avg_records.append(avg_record)
#
#     # (이름, 평균 실적)으로 이루어진 튜플의 리스트를 생성합니다.
#     sorted_members = []
#     for name, avg_record in zip(member_names, member_avg_records):
#         sorted_members.append((name, avg_record))
#
#     # 평균 실적을 기준으로 내림차순으로 멤버를 정렬합니다.
#     sorted_members.sort(key=lambda x: x[1], reverse=True)
#
#     # 보너스 대상자를 결정합니다.
#     bonus_candidates = []
#     for name, avg_record in sorted_members[:2]:
#         if avg_record > 5:
#             bonus_candidates.append(name)
#
#     # 면담 대상자를 결정합니다.
#     counseling_candidates = []
#     for name, avg_record in sorted_members[4:]:
#         if avg_record <= 3:
#             counseling_candidates.append(name)
#
#     # 결과 출력
#     print("보너스 대상자", ', '.join(bonus_candidates))
#     print("면담 대상자", ', '.join(counseling_candidates))
#
#
# # 주어진 데이터
# member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
# member_records = [
#     [4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5],
#     [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
#     [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1],
#     [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
#     [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9],
#     [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]
# ]
#
# # 함수 호출하여 결과 출력
# sales_management(member_names, member_records)


#6.3

def stock_profit(stocks, sells):
    # 종목 정보 파싱
    stock_list = stocks.split(',')
    stock_info = {}
    for stock in stock_list:
        name, quantity, buy_price = stock.split('/')
        stock_info[name] = {'quantity': int(quantity), 'buy_price': int(buy_price)}

    # 종목별 수익률 계산
    profit_rate = {}
    for i, sell_price in enumerate(sells):
        name = list(stock_info.keys())[i]
        buy_price = stock_info[name]['buy_price']
        profit_rate[name] = (sell_price - buy_price) / buy_price * 100

    # 수익률이 높은 순서대로 정렬
    sorted_profit_rate = sorted(profit_rate.items(), key=lambda x: x[1], reverse=True)

    # 결과 출력
    for name, rate in sorted_profit_rate:
        print(f"{name}의 수익률 {rate:.2f}")


# 종목 정보
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

# 함수 호출
stock_profit(stocks, sells)

# def stock_profit(stocks_info, sell_prices):
#     # 종목 정보 파싱하여 데이터 구성
#     stock_data = []
#     for stock in stocks_info.split(','):
#         stock_split = stock.split('/')
#         name = stock_split[0]
#         quantity = int(stock_split[1])
#         buy_price = int(stock_split[2])
#         stock_tuple = (name, quantity, buy_price)
#         stock_data.append(stock_tuple)
#
#     # 종목별 수익률 계산
#     profits = []
#     for i in range(len(stock_data)):
#         name, _, buy_price = stock_data[i]
#         sell_price = sell_prices[i]
#         profit = ((sell_price - buy_price) / buy_price) * 100
#         profit_tuple = (name, profit)
#         profits.append(profit_tuple)
#
#     # 수익률에 따라 내림차순으로 정렬
#     sorted_profits = []
#     for profit_tuple in profits:
#         sorted_profits.append(profit_tuple)
#     sorted_profits.sort(key=lambda x: x[1], reverse=True)
#
#     # 정렬된 결과 출력
#     for profit_tuple in sorted_profits:
#         name = profit_tuple[0]
#         profit = profit_tuple[1]
#         print(f"{name}의 수익률 {profit:.2f}")
#
#
# # 주어진 데이터
# stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
# sells = [82000, 160000, 835000, 410000]
#
# # 함수 호출하여 결과 출력
# stock_profit(stocks, sells)


# def stock_profit(stocks_info, sell_prices):
#     stocks = stocks_info.split(',')
#
#     stock_data = [stock.split('/') for stock in stocks]
#     stock_data = [(name, int(quantity), int(buy_price)) for name, quantity, buy_price in stock_data]
#
#     profits = [(name, ((sell - buy) / buy) * 100) for (name, _, buy), sell in zip(stock_data, sell_prices)]
#
#     sorted_profits = sorted(profits, key=lambda x: x[1], reverse=True)
#
#     for name, profit in sorted_profits:
#         print(f"{name}의 수익률 {profit:.2f}")
#
#
# # 주어진 데이터
# stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
# sells = [82000, 160000, 835000, 410000]
#
# # 함수 호출하여 결과 출력
# stock_profit(stocks, sells)


#6.4


def good_customer(info):
    # 회원 정보 파싱
    info_list = info.split(',')
    customer_info = {'아이디': [], '나이': [], '전화번호': [], '성별': [], '지역': [], '구매횟수': []}
    for i in range(0, len(info_list), 6):
        customer_info['아이디'].append(info_list[i])
        customer_info['나이'].append(info_list[i + 1])
        phone_number = info_list[i + 2]
        if phone_number == 'x':
            phone_number = '000-0000-0000'
        customer_info['전화번호'].append(phone_number)
        customer_info['성별'].append(info_list[i + 3])
        customer_info['지역'].append(info_list[i + 4])
        customer_info['구매횟수'].append(int(info_list[i + 5]))

    # VIP 회원 선정
    vip_customers = []
    for i in range(len(customer_info['아이디'])):
        if customer_info['구매횟수'][i] >= 8 and customer_info['전화번호'][i] != '000-0000-0000':
            vip_customers.append(i)

    # 결과 출력
    print(customer_info)
    for i in vip_customers:
        print(
            f"할인 쿠폰을 받을 회원정보 아이디:{customer_info['아이디'][i]}, 나이:{customer_info['나이'][i]}, 전화번호:{customer_info['전화번호'][i]}, 성별:{customer_info['성별'][i]}, 지역:{customer_info['지역'][i]}, 구매횟수: {customer_info['구매횟수'][i]}")



info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
good_customer(info)


