while True:
    n = int(input().strip())
    if n == -1:
        break

    if n <= 1:
        print(f"{n} is NOT perfect.")
        continue

    # 약수 구하기
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    # 약수의 합 구하기
    sum_divisors = sum(divisors)

    # 완전수 판별 및 출력
    if sum_divisors == n:
        divisors_str = " + ".join(map(str, divisors))

        # divisors_str = ""
        # for idx, divisor in enumerate(divisors):
        #     if idx > 0:
        #         divisors_str += " + "
        #     divisors_str += str(divisor)
        # 위와 같음. 근데 join() 메서드를 사용하는 방식이 보다 간결하고 파이썬 다운 방법이며, 성능 면에서도 일반적으로 더 효율적
        # 따라서 대부분의 경우 join()과 map()을 사용하는 것이 권장
        
        print(f"{n} = {divisors_str}")
    else:
        print(f"{n} is NOT perfect.")
