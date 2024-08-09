N, M = map(int, input().split())    # 가로와 세로의 길이
num_of_line = int(input())
line_arr = [list(map(int, input().split())) for _ in range(num_of_line)]
paper = [['0']*N for _ in range(M)]

# 자른 넓이를 표시하는 과정
for line in line_arr:
    if line[0] == 0:    # 가로로 자를 경우
        for i in range(line[1]):
            for j in range(N):
                paper[i][j] += 'W'    # 가로로 자른 부분의 위쪽은 W를 값으로 추가
        for i in range(line[1], M):
            for j in range(N):
                paper[i][j] += 'X'    # 아래쪽은 X를 값으로 추가
    elif line[0] == 1:    # 세로로 자를 경우
        for i in range(M):
            for j in range(line[1]):
                paper[i][j] += 'Y'   # 세로로 자른 부분의 왼쪽은 Y를 값으로
        for i in range(M):
            for j in range(line[1], N):
                paper[i][j] += 'Z'    # 오른쪽은 Z를 값으로 추가
# 잘릴 때마다 영역별로 알파벳이 누적될 것이기 때문에 최종적으로 잘렸을 때 분리된 영역들은 각각 다른 알파벳 조합을 가지고 있을 것
# '0WYW' 같은 형태

# 서로 다른 알파벳의 개수를 세는 과정
temp = []    # paper의 모든 원소들을 하나의 리스트로 만들어주기 위한 리스트
count = {}    # paper의 원소별 개수를 담기 위한 딕셔너리

for i in range(M):
    temp.extend(paper[i])    # paper의 모든 원소들을 하나의 리스트로 만들고
temp = set(temp)    # 중복된 것을 제거하기 위해 set으로 처리

for element in temp:
    count[element] = 0    # temp에 있는 요소를 count의 키로 만들고 값을 0으로 설정

for i in range(M):
    for j in range(N):    # paper의 원소를 하나씩 순회하면서
        count[paper[i][j]] += 1    # paper의 원소와 동일한 키를 가진 딕셔너리의 값을 1 추가 (개수 세기)

# 영역의 최대 크기를 구하는 과정
max_count = 0
for value in count.values():
    if value > max_count:
        max_count = value
        result = max_count

print(result)