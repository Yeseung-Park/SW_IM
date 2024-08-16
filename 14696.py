N = int(input())    # 딱지 놀이의 총 라운드 수

for _ in range(N):    # N번의 딱지놀이 동안
    temp_A = list(map(int, input().split()))    # A의 딱지로 0번째 인덱스는 제외
    A = temp_A[1:]    # 실제 A가 가지고 있는 딱지의 도형
    temp_B = list(map(int, input().split()))    # B의 딱지로 0번째 인덱스는 제외
    B = temp_B[1:]    # 실제 B가 가지고 있는 딱지의 도형
    # 0번째 인덱스는 A, B가 낸 딱지에 그려진 도형의 개수

    is_there_winner = False    # 우승자가 결정 되었는지 확인하는 변수

    # 별의 개수, 동그라미의 개수, 네모의 개수, 세모의 개수를 차례대로 비교
    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):
            winner = 'A'
            is_there_winner = True
            break    # 우승자가 결정 났으면 break 하기
        elif A.count(i) < B.count(i):
            winner = 'B'
            is_there_winner = True
            break

    if is_there_winner:    # 우승자가 존재하면
        print(winner)
    else:    # 우승자가 존재하지 않는다는 것은 무승부라는 의미
        print('D')