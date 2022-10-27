import requests
res = requests.get("http://google.com")
#res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # raise쓰면 오류 생기면 멈추고 오류 바로 출력
#print("응답코드 :", res.status_code) # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:  #여기서 w는 \쓰기모드
    f.write(res.text)