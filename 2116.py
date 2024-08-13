# 도저히 감도 안 잡히네요!
# 진짜 더러운 하드코딩이긴 한데... 어떻게 하면 더 간단하게 풀 수 있을까. 내 머리로는 이게 한계다.

import copy

N = int(input())    # 주사위의 개수
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0    # 최대 결과를 담을 변수

# 인덱스 상으로 0과 5, 1과 3, 2와 4가 마주보고 있음

# 쌓아올린 주사위 만들기
# 바닥에 올 숫자 먼저 정하기
for i in range(6):
    new_arr = copy.deepcopy(arr)
    if i == 0:
        new_arr[0][i] = 0
        next = new_arr[0][i+5]
        new_arr[0][i+5] = 0    # pop을 해주면 인덱스 에러가 나기 때문에 0으로 바꿔서 고려를 해주지 않기
    elif i == 5:
        new_arr[0][i] = 0
        next = new_arr[0][i-5]
        new_arr[0][i-5] = 0
    elif i == 1 or i == 2:
        new_arr[0][i] = 0
        next = new_arr[0][i+2]
        new_arr[0][i+2] = 0
    else:
        new_arr[0][i] = 0
        next = new_arr[0][i-2]
        new_arr[0][i-2] = 0

    for j in range(1, 5):
        if new_arr[j].index(next) == 0:
            new_arr[j][0] = 0
            next = new_arr[j][5]
            new_arr[j][5] = 0
        elif new_arr[j].index(next) == 5:
            new_arr[j][5] = 0
            next = new_arr[j][0]
            new_arr[j][0] = 0
        elif new_arr[j].index(next) == 1 or new_arr[j].index(next) == 2:
            idx = new_arr[j].index(next)
            new_arr[j][idx] = 0
            next = new_arr[j][idx + 2]
            new_arr[j][idx + 2] = 0
        else:
            idx = new_arr[j].index(next)
            new_arr[j][idx] = 0
            next = new_arr[j][idx - 2]
            new_arr[j][idx - 2] = 0

    maximum_list=[]
    for dice in new_arr:
        maximum_list.append(max(dice))

    temp = sum(maximum_list)
    if temp > result:
        result = temp

print(result)