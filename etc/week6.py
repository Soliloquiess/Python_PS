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