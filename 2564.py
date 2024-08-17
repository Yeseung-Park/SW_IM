N, M = map(int, input().split())    # N: 블록의 가로 길이, M: 블록의 세로 길이
K = int(input())    # K: 상점의 개수
stores = [list(map(int, input().split())) for _ in range(K+1)]    # 상점과 동근이의 위치 정보
# 마지막은 동근이의 위치정보다.

# GPT말대로 블록을 직선의 거리로 생각해볼까?
# 북쪽 거리 -> 동쪽 거리 -> 남쪽 거리 -> 서쪽 거리 순으로 쭉 이어진 하나의 직선인거지
block = [0]*(2*N+2*M)    # 직선으로 만든 거리
# 1~9까지는 북쪽 거리, 11~14까지는 동쪽 거리, 16~24까지는 남쪽 거리, 26~29까지는 서쪽 거리

# 직선 거리에 상점과 동근이를 위치시키는 과정
for i in range(0, K+1):
    # 마지막은 동근이로 K+1 숫자로 표현된다.
    if stores[i][0] == 1:    # 상점이 북쪽에 있을 경우
        block[stores[i][1]] = i + 1    # 상점의 번호와 일치시키기 위함
    elif stores[i][0] == 2:    # 상점이 남쪽에 있을 경우
        block[2*N+M-stores[i][1]] = i + 1    # 직선거리로 만들었기 때문에 그걸 반영
    elif stores[i][0] == 3:    # 상점이 서쪽에 있을 경우
        block[2*N+2*M-stores[i][1]] = i + 1
    elif stores[i][0] == 4:    # 상점이 동쪽에 있을 경우
        block[N+stores[i][1]] = i + 1

result = 0    # 최종 결과를 담는 변수

# 각각의 상점들과 동근이까지의 최소 거리를 구하는 과정
for i in range(1, K+1):    # 각각의 상점들에 대해서
    if block.index(K+1) > block.index(i):    # 동근이의 인덱스가 상점의 인덱스보다 크다면
        temp1 = block.index(K+1) - block.index(i)    # 임시 거리는 동근이에서 상점을 뺀 값
    else:    # 반대라면
        temp1 = block.index(i) - block.index(K+1)    # 임시거리는 어쩌구
    temp2 = 2*N+2*M - temp1    # 반대방향으로 간 거리도 확인
    if temp1 >= temp2:    # 만약 temp1이 더 크다면
        result += temp2    # temp2를 결과에 추가
    else:
        result += temp1    # 그 외의 경우에는 temp1을 결과에 추가

print(result)