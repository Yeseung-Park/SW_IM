# 직사각형 네 개의 합집합의 면적 구하기

arr = [list(map(int, input().split())) for _ in range(4)]    # 주어진 변수를 모두 하나의 리스트로 지정

total_area = set()

for i in range(4):
    square = arr[i]    # 주어진 정보 하나씩 개별의 사각형을 의미
    for j in range(square[0], square[2]):
        for k in range(square[1], square[3]):    # 이렇게 해주면 square가 포함하는 작은 사각형을 좌표로 지정해줄 수 있음
            total_area.add(f'({j}, {k})')    # 작은 사각형을 집합에 넣어줌으로써 중복된 것 제거

print(len(total_area))    # 개수 산출