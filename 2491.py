N = int(input())    # 수열의 길이
numbers = list(map(int, input().split()))    # 수열

# 연속해서 증가하는 부분을 먼저 찾는다.
increase_len = 1    # 맨 처음 원소는 일단 무조건 increse_len에 추가한다고 생각하고 시작
# 기본값이 1부터 시작인 이유는 비교할 때 자기자신을 고려하기 위해서...?
# 그 뭔가 있다 아무튼 설명하기는 어렵지만.
increase = []
for i in range(1, N):
    if numbers[i-1] <= numbers[i]:    # 연속해서 증가하는 부분이라면
        increase_len += 1    # 증가하는 부분 길이에 하나씩 추가
    else:    # 아니라면
        increase.append(increase_len)    # 현재까지의 길이를 increase에 append하고
        increase_len = 1    # 증가하는 부분 길이 초기화
increase.append(increase_len)    # 마지막의 increase_len도 넣어주기
increase_result = max(increase)    # 증가하는 부분들 중 가장 길이가 긴 걸 1차 결과로 저장

# 이번에는 연속해서 감소하는 부분을 찾는다.
# 연속해서 증가하는 부분을 찾는 것과 비슷하다.
decrease_len = 1    # 맨 처음 원소는 일단 무조건 decrease_len에 추가한다고 생각하고 시작
decrease = []
for i in range(1, N):
    if numbers[i-1] >= numbers[i]:    # 연속해서 감소하는 부분이라면
        decrease_len += 1
    else:    # 아니라면
        decrease.append(decrease_len)
        decrease_len = 1
decrease.append(decrease_len)    # 마지막의 decrease_len도 넣어주기
decrease_result = max(decrease)

result = max(increase_result, decrease_result)

print(result)