# 왼쪽 아래를 시작으로 위, 오른쪽, 아래, 왼쪽 방향으로 가면서 숫자 넣기
# 달팽이 문제와 유사    # 첫 시작을 어디로 하느냐만 다르다.
# 근데 좌석 좌표가 좀 이상하긴 하다

C, R = map(int, input().split())
K = int(input())

seats = [[0]*C for _ in range(R)]    # 좌석 만들기

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]    # 위 오른쪽 아래 왼쪽
direction = 0    # 방향을 설정하는 변수

i, j = R-1, 0    # 시작 위치 설정    # 왼쪽 아래
temp_i, temp_j = '_', '_'    # K번의 행 열 값을 담는 변수

for num in range(1, C*R+1):    # 1부터 C*R까지의 숫자가 차례로 들어간다.
    seats[i][j] = num    # 숫자 넣기
    if num == K:    # 원하는 K번을 넣었다면
        temp_i, temp_j = i, j    # 행 열 값을 가져오고
        break    # 더 탐색하지 말고 빠져나오기
    else:    # 그 외의 경우
        if 0 <= i + di[direction] < R and 0 <= j + dj[direction] < C and seats[i+di[direction]][j+dj[direction]] == 0:
            # 비어있는 자리면
            pass    # 방향 안 바꾸고 계속 탐색
        else:    # 채워져 있거나 막혀져 있는 경우
            direction = (direction + 1) % 4    # 위 오른 아 왼 방향을 반복해서 돌기 위해 나머지 연산자 사용
        # 다음 위치 저장
        i = i + di[direction]
        j = j + dj[direction]
if temp_i == '_' and temp_j == '_':    # K가 존재하지 않는 경우
    result = [0]    # 결과는 0
else:    # 존재할 경우
    result = [temp_j + 1, R - temp_i]    # 올바른 좌석 번호가 결과

print(*result)

# 채점이 너무 느린데...?
# 왜 틀림...?
# 아 0,0인 경우도 있구나