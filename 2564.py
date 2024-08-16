import pprint

def find_index(list, x):
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == x:
                return i, j
N, M = map(int, input().split())    # N: 블록의 가로의 길이, M: 블록의 세로의 길이
# 점으로 이루어진 좌표를 그냥 냅다 칸으로 나타내보기
block = [[0]*(N+1) for _ in range(M+1)]

K = int(input())    # K: 상점의 수

# 상점의 위치 표시    # 마지막 K+1번은 동근이를 나타낸다.
for i in range(1, K+2):
    direction, location = map(int, input().split())
    if direction == 1:
        block[0][location] = i
    elif direction == 2:
        block[M][location] = i
    elif direction == 3:
        block[location][0] = i
    else:
        block[location][N] = i

dong_i, dong_j = find_index(block, K+1)

# 동근이를 시작으로 좌우로 탐색하고 막히면 상하로 탐색하기
# 상점 하나씩 돌아가면서 탐색
for i in range(1, K+1):
    # 시계방향 먼저
    clockwise = 0
    direction = 0
    if dong_i == M:    # 동근이의 시작지점이 남쪽일 경우
        di = [0, -1, 0, 1]
        dj = [-1, 0, 1, 0]    # 왼 위 오 아
        for _ in range(30):    # 최대로 이동할만한 거리는 29까지
            if 0 <= dong_i + di[direction] <= M and 0 <= dong_j + dj[direction] <= N:
                if block[dong_i + di[direction]][dong_j + dj[direction]] == i:
                    clockwise += 1
                    clockwise_temp = clockwise
                    break
                else:
                    dong_i, dong_j = dong_i + di[direction], dong_j + dj[direction]
                    clockwise += 1
            else:
                direction = (direction + 1) % 4
                dong_i, dong_j = dong_i + di[direction], dong_j + dj[direction]
                clockwise += 1
    print(clockwise_temp)

pprint.pprint(block)