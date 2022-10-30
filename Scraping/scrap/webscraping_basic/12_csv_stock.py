import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")   #  newline="" 울 써서 엔터 효과(이거 안 쓰면 엔터 한줄 더 들어간 듯이 나온다.)
writer = csv.writer(f)  #writer에 파일 집어넣음

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", ...]
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip(의미없는 tr밑에 td있는거)
            continue
        data = [column.get_text().strip() for column in columns]    #get_text().strip()를 붙여 불필요한 줄바꿈 제거
        #print(data)
        writer.writerow(data) #위에있는 데이터형태 리스트형식으로 출력
    #writerow로 어떤 값을 집어넣어줌.