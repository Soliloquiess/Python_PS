def solution(numbers):
    num_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }
    
    result = ""
    temp = ""
    
    for ch in numbers:
        temp += ch
        if temp in num_map:
            result += num_map[temp]
            temp = ""
    
    return int(result)
