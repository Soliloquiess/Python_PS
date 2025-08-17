def solution(order):
    # 메뉴별 가격 딕셔너리
    price_map = {
        "americano": 4500,
        "cafelatte": 5000
    }
    
    answer = 0
    for item in order:
        item_lower = item.lower()  # 혹시 대소문자 섞여도 안전
        if "americano" in item_lower:
            answer += 4500
        elif "cafelatte" in item_lower:
            answer += 5000
        else:  # anything 같은 경우 차가운 아메리카노
            answer += 4500
    return answer
