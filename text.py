#1.

import sys

sys.stdin = open('input.txt')

# 0. ㅁㅁㄴ
# 1. 같은 크기값이 존재(중복)하면 한 상자를 배정
#     -> N//2 를 초과하는 지 체크, return
#     -> 중복 카운트값을 리스트에 저장 [[list], [cnt]]
# 2. for 반복으로 상자에 if cnt: 1씩 빼면서 다음 상자 체크
#     -> cnt == 0 일때만 배정
# 3. 각 상자의 len() 최대-최소 차이값을 검증
#     -> if v > N//2 : return 0, else: return v

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    boxes = [[[], [0]] for _ in range(3)]

    def custom(arr):
        dup_l, dup_cnt = [], []
        for x in set(arr):
            if arr.count(x) > 1:
                for x in range(arr.count(x)):
                    dup_l.append(x)
                dup_l.append(arr.count(x))
                dup_l.append([[x for _ in range(arr.count(x))], arr.count(x)])
                for _ in range(arr.count(x)):
                    arr.remove(x)
        # print(dup_l, '반복 리스트')
        if len(dup_l) > 3:
            return -1
        for i in range(len(dup_l)):
            boxes[i][0].append(dup_l[0][0])     # 리스트 추가
            boxes[i][1][0] += dup_l[0][1]       # 카운트 추가
        boxes.sort(key= lambda x: x[1], reverse=True)
        cnt_1, cnt_2, cnt_3 = boxes[0][1][0], boxes[1][1][0], boxes[2][1][0]

        while len(arr)>0 and len(dup_l)>0:
            for _ in range(cnt_1-cnt_2):
                if arr:
                    boxes[1][0].append(arr.pop())
                if arr:
                    boxes[2][0].append(arr.pop())
            break

        while len(arr)>0 and len(dup_l)>0:
            for _ in range(cnt_2-cnt_3):
                if arr:
                    boxes[2][0].append(arr.pop())
            break

        while arr:
            if arr:
                boxes[0][0].append(arr.pop())
            if arr:
                boxes[1][0].append(arr.pop())
            if arr:
                boxes[2][0].append(arr.pop())
        # print(boxes)

        max_v, min_v = -1e9, 1e9
        for box, cnt in boxes:
            # print(len(box), 'len값')
            # print(type(box[0]))
            if type(box[0]) == list:
                temp = len(box[0]) + len(box) - 1
            else:
                temp = len(box)
            if max_v < temp:
                max_v = temp
            if min_v > temp:
                min_v = temp
        # print(max_v, min_v, 'max, min 값')
        # print(N//2, '기준 값')
        if max_v > N//2:
            return -1
        return max_v - min_v

        # print(boxes[0][0][0])
        # print(boxes)

    # custom(arr)
    print(f'#{tc}', custom(arr))