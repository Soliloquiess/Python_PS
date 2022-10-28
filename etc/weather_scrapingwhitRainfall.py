import requests
from bs4 import BeautifulSoup
import re
import csv


class naverWeather():
    session = requests.Session()
    # 예전 url 주소
    # addr = "http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT"
    addr = "https://weather.naver.com/today/"
    addrAir = "https://weather.naver.com/air/"
    map_cityNum = {}
    temp_wearingFits = list()

    # csv 파일 open 후 딕셔너리, 리스트에 저장. 지역번호, 옷관련 정보 파일은 csv에 저장되어있음.
    with open('cityNumber.csv', mode='r', encoding="utf-8") as citys:
        reader = csv.reader(citys)
        map_cityNum = {rows[0]: rows[1].replace('"', '').strip() for rows in reader}

    with open('wearing.csv', mode='r', encoding="utf-8") as clothes:
        reader = csv.reader(clothes)
        temp_wearingFits = list(reader)

    def __init__(self, area):
        self.area = area
        self.addr = None
        self.addrAir = None
        self.result = None
        self.fits = list()

        cityNum = naverWeather.map_cityNum[area]
        self.addr = naverWeather.addr + cityNum
        self.addrAir = naverWeather.addrAir + cityNum

        self.search()

    # 네이버 날씨 data 크롤링
    def search(self):
        naverWeather.session.encoding = 'utf-8'

        req = naverWeather.session.get(self.addr)
        reqAir = naverWeather.session.get(self.addrAir)
        soup = BeautifulSoup(req.text, "html.parser")
        soupAir = BeautifulSoup(reqAir.text, "html.parser")
        location = soup.find(class_='location_name')
        table = soup.find(class_="week_list")
        currentWeather = soup.find(class_='weather')
        air = soupAir.find(class_='top_area')
        t_ary = list(table.stripped_strings)
        t_aryAir = list(air.stripped_strings)


        self.result = ("[" + self.area + "(" + location.text + ")" + " 날씨 검색 결과]\n"
                       + "- 오늘(" + t_ary[1] + ")\n"
                       + " \t 오전 - " + t_ary[11][:-1] + "℃ (" + t_ary[5] + ", 강수확률 : " + t_ary[4] + ")\n"
                       + " \t 오후 - " + t_ary[14][:-1] + "℃ (" + t_ary[9] + ", 강수확률 : " + t_ary[8] + ")\n"
                       + " \t 미세먼지 - " + t_aryAir[15] + "㎍/㎥ (" + t_aryAir[16] + ")\n"
                       + " \t 초미세먼지 - " + t_aryAir[32] + "㎍/㎥ (" + t_aryAir[33] + ")\n"
                       + " \t 현재 날씨상태 - " + currentWeather.text + "\n" + self.needUmbrella(currentWeather.text)
                       + "- 내일(" + t_ary[16] + ")\n"
                       + " \t 오전 - " + t_ary[26][:-1] + "℃ (" + t_ary[20] + ", 강수확률 : " + t_ary[19] + ")\n"
                       + " \t 오후 - " + t_ary[29][:-1] + "℃ (" + t_ary[24] + ", 강수확률 : " + t_ary[23] + ")\n")

        self.fits = self.recommandFits(t_ary)

    # 기온에 맞게 옷 정보를 반환
    def recommandFits(self, t_ary):
        fits = list()
        avr = (int(t_ary[11][:-1]) + int(t_ary[14][:-1])) / 2

        if (avr >= 28.0):
            fits = self.temp_wearingFits[0]
        elif (avr >= 27.0):
            fits = self.temp_wearingFits[1]
        elif (avr >= 20.0):
            fits = self.temp_wearingFits[2]
        elif (avr >= 17.0):
            fits = self.temp_wearingFits[3]
        elif (avr >= 12.0):
            fits = self.temp_wearingFits[4]
        elif (avr >= 9.0):
            fits = self.temp_wearingFits[5]
        elif (avr >= 5.0):
            fits = self.temp_wearingFits[6]
        elif (avr <= 4.0):
            fits = self.temp_wearingFits[7]

        return fits

    def needUmbrella(self, currentWeather):
        if currentWeather == '비':
            return "\n\t *오늘같은 날은 우산을 챙기는건 어때요?\n\n"
        else:
            return "\n\t *우산이 필요없을거 같아요!\n\n"

    def getWeather(self):
        if not self.result:
            # 도시명을 잘못 입력한 경우 결과가 나오지 않는다.
            return "잘못된 도시명입니다"
        return self.result

    def getFits(self):
        if not self.fits:
            return "기온이 잘못되었습니다."
        return self.fits


while True:
    print("\n날씨를 알고 싶은 도시명을 입력하세요(ex: 서울, 제주) : ", end="")
    print("\nq를 누르면 종료합니다.")
    print(">> ", end="")
    city = input()
    print("\n")

    if city == "q":
        print("종료.")
        break
    if city not in naverWeather.map_cityNum:
        print("잘못된 도시명입니다.")
        continue

    temp = naverWeather(city)

    print(temp.getWeather())
    print("====== 오늘 기온에 맞는 옷 추천 ======")
    for fits in temp.getFits():
        print(fits.replace('"', '').strip())