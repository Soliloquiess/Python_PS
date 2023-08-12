# 작성자: Karu_리드부스터

# 주민등록번호 확인 함수
def check_id(id: str):
  try:
    validate(id)
    gender = get_gender(id)

    birth = ''
    if int(id[:2]) in [*range(24)]:             # 생년이 00~23인 경우
      birth = check_and_get_birth(id)           # 2000년 이후 출생자인지 확인
    else:                                       # 그 외의 경우엔 별도로 확인하지 않음
      birth = '19' + id[:2]
    print(f'{birth}년 {id[2:4]}월 {gender}')

  except ValueError:                            # 입력값 오류가 났다면 종료
    print('잘못된 번호입니다. \n올바른 번호를 넣어주세요.')
    exit()

# 형식 검증
def validate(id: str):
  if '-' not in id:                     # 하이픈이 포함되어 있는가?
    raise ValueError
  head, tail = id.split('-')
  if len(head) != 6 or len(tail) != 7:  # 길이가 올바른가?
    raise ValueError

# 성별을 반환하는 함수
def get_gender(id: str) -> str:
  return '남자' if (int(id[7]) & 1 == 1) else '여자'

def check_and_get_birth(id: str) -> str:
  while True:
    match input('2000년 이후 출생자입니까? (O/X) >> '):
      case 'o' | 'O' if id[7] in "34":  # 2000년 이후이고 뒷자리 시작번호가 3, 4
        return '20' + id[:2]
      case 'x' | 'X' if id[7] in "12":  # 2000년 이전이고 뒷자리 시작번호가 1, 2
        return '19' + id[:2]
      case 'o' | 'O' | 'x' | 'X':       # 위에 해당하지 않는 경우
        raise ValueError
      case _:                           # 그냥 엉뚱한 값을 입력한 경우
        print('다시 입력해주세요.')


# 사용자로부터 주민등록번호 입력받기
a = input('주민등록번호를 입력해주세요 >> ')
check_id(a)