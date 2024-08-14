N = int(input())
columns = [list(map(int, input().split())) for _ in range(N)]

# 우선 기둥을 왼쪽에서부터 순서대로 정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if columns[j][0] > columns[j+1][0]:
            columns[j], columns[j+1] = columns[j+1], columns[j]

# 여기서부터는 GPT가 힌트를 줬다.
# 하지만 내가 원래 생각한 방법이랑 비슷한 것 같다.

# 먼저 가장 높은 기둥을 찾는다.
# 가장 높은 기둥을 기준으로 좌우로 나누어 넓이를 구할 것이므로 가장 높은 기둥의 column 상에서 인덱스도 추출한다.
max_height = 0
for i in range(N):
    if columns[i][1] > max_height:
        max_height = columns[i][1]
        std_idx = i

# 가장 높은 기둥을 기준을 좌우로 나누어 넓이를 구하기
# 왼쪽의 경우 왼쪽부터, 오른쪽의 경우 오른쪽부터 차례대로 넓이를 구하기
# 만약 더 높은 기둥을 만났을 경우 해당 기둥으로 이어서 구하기
# 다른 사람이 보면 이해를 못 할 것 같지만 내가 쓴거니 나는 이해가 된다

area = 0    # 전체 넓이를 담는 변수

# 왼쪽 부분 넓이 구하기
# 가장 높은 기둥을 기준으로 넓이를 구해야하기 때문에 매번 가장 높은 기둥의 높이를 찾아줘야 한다.
left_height = 0
for i in range(0, std_idx):
    if columns[i][1] > left_height:    # 기존 기둥보다 더 높은 기둥을 만나면
        left_height = columns[i][1]    # 가장 높은 기둥 값을 갱신해주고
        area += (columns[i+1][0] - columns[i][0]) * left_height    # 다음 기둥이 나올 때까지 쭉 해당 높이로 넓이 계산
    else:    # 더 높은 기둥이 아닐 경우
        area += (columns[i+1][0] - columns[i][0]) * left_height    # 그냥 기존 기둥 높이로 넓이 계산

# 오른쪽 부분 넓이 구하기
right_height = 0
for i in range(N-1, std_idx, -1):
    if columns[i][1] > right_height:
        right_height = columns[i][1]
        area += (columns[i][0] - columns[i-1][0]) * right_height
    else:
        area += (columns[i][0] - columns[i-1][0]) * right_height

# 마지막 제일 높은 기둥의 넓이 더하기
area += max_height

print(area)
