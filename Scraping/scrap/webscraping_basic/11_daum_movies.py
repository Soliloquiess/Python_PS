import requests
from bs4 import BeautifulSoup

for year in range(2018, 2022):  #2018부터 2021까지
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)    
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:    #wb인 이유는 영화파일 말고 이미지 이런거도 있어서
            #바이너리를 의미하는 b까지 붙여서 wb로 준다.
            #{},{} 각 문자열 스트링 안에 year, idx정보 넣어준다.
            f.write(image_res.content)  #파일에 쓰고 파일에 쓸 내용은 content(이 컨텐츠가 이미지)

        if idx >= 4: # 상위 5개 이미지까지만 다운로드(인덱스가 4보다 크면 탈출)
            break