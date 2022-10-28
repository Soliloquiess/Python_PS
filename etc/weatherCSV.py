import requests
from bs4 import BeautifulSoup
import re
import csv

session = requests.Session()
# 예전 url 주소
# addr = "http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT"
addr = "https://weather.naver.com/today/"
addrAir = "https://weather.naver.com/air/"
session.encoding = 'utf-8'
map_cityNum = {}
temp_wearingFits = list()

# csv 파일 open 후 딕셔너리, 리스트에 저장. 지역번호, 옷관련 정보 파일은 csv에 저장되어있음.
with open('cityNumber.csv', mode='r', encoding="utf-8") as citys:
    reader = csv.reader(citys)
    map_cityNum = {rows[0]: rows[1].replace('"', '').strip() for rows in reader}

with open('wearing.csv', mode='r', encoding="utf-8") as clothes:
    reader = csv.reader(clothes)
    temp_wearingFits = list(reader)


def search(city):
    cityNum = map_cityNum[city]
    address = addr + cityNum
    addressAir = addrAir + cityNum

    req = session.get(address)
    reqAir = session.get(addressAir)
    soup = BeautifulSoup(req.text, 'html.parser')
    soupAir = BeautifulSoup(reqAir.text, "html.parser")
    location = soup.find(class_='location_name')
    table = soup.find(class_="week_list")
    water = soup.find(class_="rainfall ")
    currentWeather = soup.find(class_='weather')
    air = soupAir.find(class_='top_area')
    t_ary = list(table.stripped_strings)
    t_aryAir = list(air.stripped_strings)

    result = ("[" + city + "(" + location.text + ")" + " 날씨 검색 결과]\n"
              + "오전 - " + t_ary[11][:-1] + "℃ (" + t_ary[5] + ", 강수확률 : " + t_ary[4] + ")\n"
              + "오후 - " + t_ary[14][:-1] + "℃ (" + t_ary[6] + ", 강수확률 : " + t_ary[9] + ")\n"
              + "미세먼지 - " + t_aryAir[15] + "㎍/㎥ (" + t_aryAir[16] + ")\n"
              + "초미세먼지 - " + t_aryAir[32] + "㎍/㎥ (" + t_aryAir[33] + ")\n"
              + "현재 날씨상태 - " + currentWeather.text + umbrella(currentWeather.text))
    return result


def umbrella(currentWeather):
    if currentWeather == '비':
        return "\n*비오니깐 우산챙겨요!"
    else:
        return "\n*우산이 필요없을거 같아요!"

if __name__ == "__main__":
    search("가평")  # 오늘의 날씨정보


# def todayRecommandFits(t_ary):
#     fits = list()
#     avr = (int(t_ary[11][:-1]) + int(t_ary[14][:-1])) / 2

#     if (avr >= 28.0):
#          fits = temp_wearingFits[0]
#     elif (avr >= 27.0):
#         fits = temp_wearingFits[1]
#     elif (avr >= 20.0):
#         fits = temp_wearingFits[2]
#     elif (avr >= 17.0):
#         fits = temp_wearingFits[3]
#     elif (avr >= 12.0):
#         fits = temp_wearingFits[4]
#     elif (avr >= 9.0):
#         fits = temp_wearingFits[5]
#     elif (avr >= 5.0):
#         fits = temp_wearingFits[6]
#     elif (avr <= 4.0):
#         fits = temp_wearingFits[7]

#     return fits