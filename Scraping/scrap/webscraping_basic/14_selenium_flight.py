from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동




# 여행 갈 나라 클릭
travel_country=browser.find_elements(By.CSS_SELECTOR,'div.tabContent_routes__laamB button')
travel_country[1].click()
# 여행 갈 나라 카테고리 클릭
category_all=browser.find_elements(By.CSS_SELECTOR,'div.autocomplete_content__3RhAZ > section.section  button')
category_all[1].click()
#여행 갈 나라 카테고리 안 서브 카테고리 클릭
subcategory_all=browser.find_elements(By.CSS_SELECTOR,'div.autocomplete_list__de1dI button')
subcategory_all[0].click()
 
# 가는 날 클릭
browser.find_element(By.CLASS_NAME,'tabContent_option__2y4c6').click()
month=browser.find_elements(By.CSS_SELECTOR,'div.sc-jrsJWt.dJdFwe.awesome-calendar div.sc-kEqXSa.bAVzgZ.month') # 11월 ~ 2022년 12월까지의 month 데이터 추출[12월추출[]] 
go_weeks=month[1].find_elements(By.CSS_SELECTOR,'table tbody tr') # 각 주차 별 데이터  [12월 데이터 추출] 
go_days=go_weeks[3].find_elements(By.CSS_SELECTOR,'td')           # 각 일 별 데이터 추출(2주차의 일요일 ~ 월요일 데이터추출) 
go_days[4].click()   # 2주차의 3번째 일 클릭 
# day=days[1].find_element_by_css_selector('button')
 
#오는 날 클릭
back_weeks=month[1].find_elements(By.CSS_SELECTOR,'table tbody tr') # 2022년 1월 1주 ~ 5주차 데이터 추출 
back_days=back_weeks[4].find_elements(By.CSS_SELECTOR,'td') # 2022년 5주차의 일요일~월요일 데이터 추출
back_days[1].click()
 
#항공권 검색하기
Filght_click=browser.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/button')
Filght_click.click()






# # 가는 날 선택 클릭
# # browser.find_element_by_link_text("가는날 선택").click()
# browser.find_element(By.LINK_TEXT, "가는 날 선택").click()

# # 이번달 27일, 28일 선택
# # browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# # browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# # 다음달 27일, 28일 선택
# # browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# # browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# # 이번달 27일, 다음달 28일 선택
# # browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements(By.LINK_TEXT,"28")[1].click() # [1] -> 다음달
# # browser.find_element(By.LINK_TEXT, "가는 날 선택").click()

# # 제주도 선택
# # browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
# browser.find_element(By.XPATH,"//*[@id='recommendationList']/ul/li[1]").click()

# # 항공권 검색 클릭
# # browser.find_element_by_link_text("항공권 검색").click()
# browser.find_element(By.LINK_TEXT,"항공권 검색").click()








try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # WebDriverWait 로 10초동안 기다림
    # 성공했을 때 동작 수행    
    # presence_of_element_located 는 어떤 엘리먼트가 나올떄까지라는 뜻 위 문구는 해당 element가 위치 할 때까지 기다려 달라는 듯.
    # By.XPATH . //*[@id='content']/div[2]/div/div[4]/ul/li[1]
    # 브라우저를 10초동안 대기 하는데 뒤 XPATH값에 해당하는 element가 나올떄 까지

    # 이외 xpath 말고도  id,class_name, Link_text등 다 가능ㄴ


    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
