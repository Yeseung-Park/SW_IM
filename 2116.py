N = int(input())    # 주사위의 개수
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0    # 최대 결과를 담을 변수

pairs = [5, 3, 4, 1, 2, 0]    # i를 인덱스로 가지는 숫자는 pairs[i]를 인덱스로 가지는 숫자와 마주보고 있다.

# 첫 번째 주사위의 아랫면을 설정하는 순간 그 이후 주사위의 모든 윗면과 아랫면은 결정이 된다.
# 따라서 첫 번째 주사위의 아랫면에 따라 경우의 수가 나누어진다고 할 수 있다.
for i in range(6):    # 첫번째 주사위가 가질 수 있는 bottom이 총 6가지
    sum_side = 0    # 옆면의 합은 첫 번째 주사위가 가지는 bottom이 달라질 때마다 초기화
    top = arr[0][pairs[i]]    # 첫 번째 주사위의 윗면

    # 이렇게 첫번째 주사위의 bottom을 정해놓고 나면 나머지 주사위는 자동으로 결정된다.
    for j in range(N):    # 두 번째 주사위가 아니라 첫 번째 주사위라고 하는 이유는 첫 번째 주사위부터
        bottom = top    # 다음 주사위의 bottom은 이전 주사위의 top
        top_index = arr[j].index(bottom)    # top으로 와야할 숫자의 인덱스 찾기
        top = arr[j][pairs[top_index]]    # 새로운 top 정하기
        # 위에서 분명 첫 번째 주사위의 bottom과 top을 정했는데 다시 정하는 이유는 이래야 나머지 주사위에 대해서도 똑같은 for문으로 접근할 수 있기 때문...

        side = []    # top과 bottom을 제외한 나머지 숫자들, 즉 옆면이 되는 숫자들을 담을 리스트
        for num in arr[j]:
            if num not in [top, bottom]:
                side.append(num)

        side_max = max(side)    # 옆면 중 제일 큰 값 찾기
        sum_side += side_max    # 다 더하기

    if sum_side > result:    # 현재 경우의 옆면의 합이 기존 결과보다 더 크면
        result = sum_side    # 그걸 새로운 결과로 지정
    # 이렇게 하면서 최댓값을 결과로 지정


print(result)