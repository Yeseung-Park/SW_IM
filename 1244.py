N = int(input())    # 스위치의 개수
arr = list(map(int, input().split()))    # 스위치의 처음 상태
M = int(input())    # 학생의 수
student = [list(map(int, input().split())) for _ in range(M)]    # 각 학생의 성별과 받은 수를 나타내는 리스트

for i in range(M):    # 각 학생들에 대해서
    if student[i][0] == 1:    # 학생의 성별이 남자라면
        for j in range(N):    # 모든 스위치에 대해서
            if (j+1) % student[i][1] == 0:    # 만약 스위치의 번호가 주어진 숫자의 배수라면
                if arr[j] == 1:    # 해당 스위치를 상태에 따라 끄거나 킨다
                    arr[j] = 0
                else:
                    arr[j] = 1
    if student[i][0] == 2:    # 학생의 성별이 여자라면
        change_section = [student[i][1]]*2    # 스위치를 변화할 구간의 시작과 끝을 담는 리스트로 초기 값은 학생이 가진 숫자
        for j in range(N):
            if 0 <= (student[i][1]-1)-j and (student[i][1]-1)+j <= N-1:    # 대칭으로 탐색할 인덱스가 범위 안에 있으면
                if arr[(student[i][1]-1)-j] == arr[(student[i][1]-1)+j]:    # 실제로 대칭이면
                    change_section[0] = (student[i][1]-1)-j    # 구간의 시작과 끝으로 설정
                    change_section[1] = (student[i][1]-1)+j
                else:    # 대칭이 아니면
                    break    # 그냥 빠져나오기
            else:    # 인덱스를 넘어서면
                break    # 빠져나오기
        for k in range(change_section[0], change_section[1]+1):    # 대칭인 구간에 대해서
            if arr[k] == 1:    # 해당 구간의 스위치를 상태에 따라 끄거나 킨다
                arr[k] = 0
            else:
                arr[k] = 1

for i in range(0, len(arr), 20):    # 조건대로 결과 출력
    print(*arr[i:i+20])