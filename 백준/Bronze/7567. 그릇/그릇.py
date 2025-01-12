def calculate_height(dishes):
    total_height = 10
    
    for i in range(1, len(dishes)):
        if dishes[i] == dishes[i-1]:
            total_height += 5
        else:
            total_height += 10
    
    return total_height

input_data = input().strip()
print(calculate_height(input_data))
