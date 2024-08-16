def count_value(list, x):    # list: 구하고자 하는 이중 리스트, x: 찾고자 하는 값
    # 이중리스트에서 원하는 요소 개수 구하는 함수
    count = 0
    for sublist in list:
        count += sublist.count(x)
    return count

board = [[0]*1001 for _ in range(1001)]    # 색종이가 놓일 격자판 생성
N = int(input())    # 색종이의 개수

# 기본적인 생각은 먼저 놓이는 사각형을 차례대로 1, 2, 3으로 넓이 체크하고
# 마지막에 해당 넓이 개수를 카운트하면 됨
# 뭔 말인지 모르겠지 난 알아... 내가 쓴 코드니까...

for num in range(1, N+1):    # 사각형을 하나씩 볼 때마다 넓이 표시는 1, 2, 3으로 하고...
    x, y, r, c = map(int, input().split())    # x: 시작점의 x좌표, y: 시작점의 y좌표, r: 너비, c: 높이
    i = 1000 - y
    j = x    # 실제 board상의 인덱스 값으로는 이렇다
    for i in range(1000-y, 1000-y-c, -1):
        for j in range(x, x+r):
            board[i][j] = num    # 이렇게 함으로써 뒤에 있어서 가려지는 사각형을 반영 가능

for num in range(1, N+1):
    result = count_value(board, num)
    print(result)

# 근데 굉장히 느리네
# pypy로 하면 100점!