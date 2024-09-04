def count_open_windows(N):
    count = 0
    i = 1
    while i * i <= N:
        count += 1
        i += 1
    return count

N = int(input())
print(count_open_windows(N))
