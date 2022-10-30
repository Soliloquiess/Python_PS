import time
from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome() # "./chromedriver.exe"
# 이렇게 하면 현재 폴더에 있는 크롬 드라이버 사용 만약 크롬 드라이버 위치가 c폴더면 
#C:\ 이렇게 넣으면 됨 아무것도 안쓰면 현 위치
#크롬 드라이버 객체 생성하고 네이버 url로 이동
# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
# elem = browser.find_element_by_class_name("link_login")
elem = browser.find_element(By.CLASS_NAME, 'link_login') 
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID,"id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")

# browser.find_element_by_id("id").send_keys("naver_id")
# browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID,"log.login").click()

# browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
#browser.find_element_by_id("id").send_keys("my_id")
browser.find_element(By.ID,"id").clear()
browser.find_element(By.ID,"id").send_keys("my_id")
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
# browser.quit() # 전체 브라우저 종료