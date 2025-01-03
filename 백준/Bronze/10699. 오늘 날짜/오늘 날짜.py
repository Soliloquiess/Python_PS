import time

# 현재 UTC 시간 (초 단위로)
utc_time = time.gmtime()

# UTC 시간을 서울 시간으로 변환 (UTC + 9시간)
seoul_time = time.gmtime(time.mktime(utc_time) + 9 * 3600)

# 년, 월, 일 추출
year = seoul_time.tm_year
month = seoul_time.tm_mon
day = seoul_time.tm_mday

# 결과 출력
print(f"{year:04d}-{month:02d}-{day:02d}")
