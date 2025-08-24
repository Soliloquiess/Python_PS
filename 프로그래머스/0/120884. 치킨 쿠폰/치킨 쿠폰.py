def solution(chicken):
    service_chicken = 0
    coupons = chicken

    while coupons >= 10:
        new_chicken = coupons // 10
        service_chicken += new_chicken
        coupons = new_chicken + (coupons % 10)

    return service_chicken
