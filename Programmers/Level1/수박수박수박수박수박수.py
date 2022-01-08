def solution(n):
    sb_list = []
    for i in range(n):
        if i % 2 == 0:
            sb_list.append("수")
        else:
            sb_list.append("박")

    sb = "".join(sb_list)

    return sb


# def solution(n):
#     return "수박"*(n//2) + "수"*(n%2)

print(solution(13))