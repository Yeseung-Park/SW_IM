# 교수님이 푼 코드

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선 수

    counts = [0] * 5001    # 5000번 정류장까지    # 정류장 번호와 인덱스를 동일하게 하기 위해 5001
    # N개의 노선 정보를 모두 읽어놓고 처리 or 읽을 때마다 처리
    for _ in range(N):
        A, B = map(int, input().split())    # Ai -> Bi 버스 노선의 시점 Ai와 종점 Bi, Ai <= Bi
        for i in range(A, B+1):    # 1 <= Ai <= Bi <= 5000
            counts[i] += 1

    P = int(input())    # 노선수를 출력할 P개의 버스 정류장
    # 모두 읽어놓고 처리
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end = ' ')
    # for j in busstop:    # 노선수를 출력할 P)