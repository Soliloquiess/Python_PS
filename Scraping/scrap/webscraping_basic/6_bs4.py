import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) # soup 객체에서 처음 발견되는 a element 출력(원래는 div> div> 이런식으로 계속 가는게 정석
print(soup.a.attrs) # a element 의 속성 정보를 출력
print(soup.a["href"]) # a element 의 href 속성 '값' 정보를 출력(attr 속성 )

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element 를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))  #soup.find하는데 클래스가 랭크 01이였던거 다 가져옴
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())      #랭크 1등에 해당하는 a태그 글자 가져옴
# print(rank1.next_sibling)  #이렇게만 하면 출력 안됨. .next_sibiling을 한번 더 들어가야됨.
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") #이러면 다음 개행 상관 없이 다음 li링크 찾는다.
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

# webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마")
# print(webtoon)