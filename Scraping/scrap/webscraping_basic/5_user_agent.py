# import requests
# url = "http://demo.initech.com/"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# with open("nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)


from selenium import webdriver
from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element(By.ID,"detected_value")
print(detected_value.text)
browser.quit()