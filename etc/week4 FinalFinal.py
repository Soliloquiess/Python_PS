#  4.1

def custom_number_format(number):
    number_str = str(number)
    length = len(number_str)
    if length <= 3:
        return number_str

    formatted_str = ""
    count = 0

    sign = ""
    if number_str[0] == "-":
        sign = "-"
        number_str = number_str[1:]
        length = len(number_str)

    for i in reversed(number_str):
        formatted_str = i + formatted_str
        count += 1
        if count % 3 == 0 and count != length:
            formatted_str = "," + formatted_str

    return sign + formatted_str


user_input = int(input("숫자를 입력하세요: "))

formatted_result = custom_number_format(user_input)
print("결과:", formatted_result)


# 4.2

def count_word(text, target_word):
    word_count = text.count(target_word)
    return word_count


def main():
    user_input = input("문장을 입력하세요: ")
    target_word = input("찾고자 하는 단어를 입력하세요: ")

    word_count = count_word(user_input, target_word)
    print(f"'{target_word}'의 개수: {word_count}")

    with open("word_count_result.txt", "w") as file:
        file.write(f"'{target_word}'의 개수: {word_count}")


if __name__ == "__main__":
    main()

# 4.3

def check_phone_number(phone_number):
    if not phone_number.startswith("010") or len(phone_number) != 13:
        return False

    groups = phone_number.split("-")
    if len(groups) != 3 or len(groups[0]) != 3 or len(groups[1]) != 4 or len(groups[2]) != 4:
        return False

    return True


def wrong_phone_book(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        entries = file.readlines()

    for entry in entries:
        name, phone_number = entry.strip().split(",")

        if not check_phone_number(phone_number):
            print(f"잘못 쓴 사람: {name}")
            print(f"잘못 쓴 번호: {phone_number}\n")


file_path = "guest_book.txt"
wrong_phone_book(file_path)

#guest_book.txt
# 김갑,123456789
# 이을,010-1234-5678
# 박병,010-5678-111
# 최정,111-1111-1111
# 정무,010-3333-3333

# 4.4

def isleapyear(year):
    if year >= 0:
        return year % 400 == 0 or \
               year % 4 == 0 and year % 100 != 0
    else:
        return None


def is_valid_date(year, month, day):
    if (year >= 0 and 1 <= month <= 12 and \
            ((month == 1 or month == 3 or month == 5 or month == 7 or
              month == 8 or month == 10 or month == 12) and
             1 <= day <= 31 or
             (month == 4 or month == 6 or month == 9 or month == 11) and
             1 <= day <= 30 or
             isleapyear(year) and 1 <= day <= 29 or
             1 <= day <= 28)):
        return True;
    else:
        return False;


def validate_jumin(jumin):
    if len(jumin) == 14:
        if jumin[6] != '-' or not jumin[:6].isdigit() or not jumin[7:].isdigit():
            return False
        else:
            return True;
    else:
        return False
    # return True


def determine_gender(jumin):
    gender_code = int(jumin[7])
    if gender_code == 1 or gender_code == 3:
        return "남성"
    elif gender_code == 2 or gender_code == 4:
        return "여성"
    else:
        return


def get_birth_year(jumin, year, month):

    if month >= 1 and month <= 12:
        century = jumin[7]  # 주민등록번호 뒷자리 시작번호
        if century == '1' or century == '2':
            year += 1900
        elif century == '3' or century == '4':
            year += 2000
        else:
            return False;
        return year
    else:
        return False;


def main():
    jumin = input("주민등록번호를 입력하세요: ")

    if len(jumin) == 13 and "-" not in jumin:
        jumin = jumin[:6] + '-' + jumin[6:]

    if not validate_jumin(jumin):
        print("잘못된 주민번호입니다")
        return

    gender = determine_gender(jumin)
    year = int(jumin[:2])
    month = int(jumin[2:4])
    day = int(jumin[4:6])
    validDate = is_valid_date(year, month, day)
    if not validDate:
        print("잘못된 날짜입니다.")
        return
    birth_year = get_birth_year(jumin, year, month)

    if not birth_year:
        print("잘못된 주민번호입니다.")
        return

    print(f"태어난 년도: {birth_year}년")
    print(f"성별: {gender}")


if __name__ == "__main__":
    main()

