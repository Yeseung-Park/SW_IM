def get_index(list, x, N=5):    # 빙고 판에서 원하는 숫자의 인덱스를 찾는 함수
    for i in range(N):
        for j in range(N):
            if list[i][j] == x:
                return i, j

board = [list(map(int, input().split())) for _ in range(5)]    # 빙고판 만들기
numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))    # 사회자가 불러주는 번호 받아오기
bingo = 0    # 빙고 개수를 저장하는 변수
number_count = 0    # 사회자가 부른 번호의 개수

for number in numbers:    # 사회자가 불러주는 번호를 차례로 하나씩 순회
    number_count += 1
    i, j = get_index(board, number)
    board[i][j] = 'O'    # 불러주는 번호를 빙고판에 O로 표시

    # 해당 숫자가 포함된 행과 열의 숫자가 모두 'O'인지 확인하고 맞으면 빙고 처리
    # 행 먼저 확인
    row_check, col_check, diag_left_check, diag_right_check = 0, 0, 0, 0
    # 가로, 세로, 왼쪽 아래 대각선, 오른쪽 아래 대각선의 빙고 여부를 확인하는 변수

    # 가로, 세로 방향 체크
    for col in range(5):
        if board[i][col] != 'O':
            break
        else:
            row_check += 1
    for row in range(5):
        if board[row][j] != 'O':
            break
        else:
            col_check += 1

    # 만약 board[i][j]가 대각선 위에 있는 숫자라면 대각선 방향도 체크
    if i == j:
        for row, col in [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]:
            if board[row][col] != 'O':
                break
            else:
                diag_right_check += 1
    if 4-i == j:
        for row, col in [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]:
            if board[row][col] != 'O':
                break
            else:
                diag_left_check += 1

    # 빙고인지 확인
    if row_check == 5:
        bingo += 1
    if col_check == 5:
        bingo += 1
    if diag_left_check == 5:
        bingo += 1
    if diag_right_check == 5:
        bingo += 1

    if bingo >= 3:    # 3빙고 이상이 완성되면 끝내기
        break

print(number_count)