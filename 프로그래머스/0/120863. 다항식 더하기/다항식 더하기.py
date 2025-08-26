def solution(polynomial):
    tokens = polynomial.split(" + ")
    x_sum = 0
    num_sum = 0

    for term in tokens:
        if "x" in term:
            if term == "x":
                x_sum += 1
            else:
                x_sum += int(term[:-1])
        else:
            num_sum += int(term)

    result = ""
    if x_sum > 0:
        if x_sum == 1:
            result += "x"
        else:
            result += str(x_sum) + "x"

    if num_sum > 0:
        if result != "":
            result += " + "
        result += str(num_sum)

    return result
