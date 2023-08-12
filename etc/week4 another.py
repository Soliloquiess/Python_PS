

def check_id(id: str):
  try:
    validate(id)
    gender = get_gender(id)

    if int(id[:2]) in [*range(24)]:
      birth = check_and_get_birth(id)
      print(f'{birth}년 {id[2:4]}월 {gender}')

  except ValueError:
    print('잘못된 번호입니다. \n올바른 번호를 넣어주세요.')
    exit()

def validate(id: str):
  if '-' not in id: # 대시가 포함되어 있는가?
    raise ValueError
  head, tail = id.split('-')
  if len(head) != 6 or len(tail) != 7: # 길이가 올바른가?
    raise ValueError

def get_gender(id: str) -> str:
  return '남자' if (int(id[7]) & 1 == 1) else '여자'

def check_and_get_birth(id: str) -> str:
  while True:
    match input('2000년 이후 출생자입니까? (O/X) >> '):
      case 'o' | 'O' if id[7] in "34":
        return '20' + id[:2]
      case 'x' | 'X' if id[7] in "12":
        return '19' + id[:2]
      case 'o' | 'O' | 'x' | 'X':
        raise ValueError
      case _:
        print('다시 입력해주세요.')

# 사용자로부터 주민등록번호 입력받기
a = input('주민등록번호를 입력해주세요 >> ')
check_id(a)