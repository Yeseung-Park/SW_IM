N = int(input())

total_result = []

for i in range(1, N+1):
    result = []
    result.append(N)
    result.append(i)

    for j in range(N):
        next_num = result[j] - result[j+1]
        if next_num >= 0:
            result.append(next_num)
        else:
            total_result.append(result)
            break

max_len = 0

for arr in total_result:
    if len(arr) > max_len:
        max_len = len(arr)
        result = arr

print(len(result))
print(*result)