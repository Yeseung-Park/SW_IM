N, K = map(int, input().split())    # N: 학생 수, K: 한 방에 배정할 수 있는 인원 수
students = {'1_w': 0, '1_m': 0,
            '2_w': 0, '2_m': 0,
            '3_w': 0, '3_m': 0,
            '4_w': 0, '4_m': 0,
            '5_w': 0, '5_m': 0,
            '6_w': 0, '6_m': 0}    # 학년별 / 성별별 학생 수를 담을 딕셔너리

for _ in range(N):    # 학년별 성별별로 나누기    # 이게 맞나;;
    S, Y = map(int, input().split())
    if S == 0 and Y == 1:
        students['1_w'] += 1
    elif S == 1 and Y == 1:
        students['1_m'] += 1
    elif S == 0 and Y == 2:
        students['2_w'] += 1
    elif S == 1 and Y == 2:
        students['2_m'] += 1
    elif S == 0 and Y == 3:
        students['3_w'] += 1
    elif S == 1 and Y == 3:
        students['3_m'] += 1
    elif S == 0 and Y == 4:
        students['4_w'] += 1
    elif S == 1 and Y == 4:
        students['4_m'] += 1
    elif S == 0 and Y == 5:
        students['5_w'] += 1
    elif S == 1 and Y == 5:
        students['5_m'] += 1
    elif S == 0 and Y == 6:
        students['6_w'] += 1
    elif S == 1 and Y == 6:
        students['6_m'] += 1

room = 0    # 필요한 방의 수를 담는 변수
for key in students.keys():
    room += -(-(students[key])//K)    # 무조건 올림

print(room)