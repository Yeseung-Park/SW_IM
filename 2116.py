# 도저히 감도 안 잡히네요!

N = int(input())    # 주사위의 개수
arr = [list(map(int, input().split())) for _ in range(N)]
dices = []

for dice in arr:
    dices.append([(dice[0], dice[5]), (dice[1], dice[3]), (dice[2], dice[4])])

print(dices)

