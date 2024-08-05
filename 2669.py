# 직사각형 네 개의 합집합의 면적 구하기

arr = [list(map(int, input().split())) for _ in range(4)]

total_area = set()

for i in range(4):
    square = arr[i]
    for j in range(square[0], square[2]):
        for k in range(square[1], square[3]):
            total_area.add(f'({j}, {k})')

print(len(total_area))