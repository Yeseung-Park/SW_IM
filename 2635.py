N = int(input())

total_result = []    # 최종 결과를 집어 넣어 줄 리스트

for i in range(1, N+1):    # 두 번째 숫자로 가능한 모든 경우에 대해서 진행
    temp_result = [N, i]    # 첫 번째 숫자와 두 번째 숫자 먼저 넣어주기

    while True:
        next_num = temp_result[-2] - temp_result[-1]    # 다음으로 들어갈 요소는 temp_result의 마지막에서 두 번째 요소와 마지막 요소의 차
        if next_num >= 0:    # 만약 다음으로 들어갈 요소가 음수가 아니라면
            temp_result.append(next_num)    # 정상적으로 집어넣기
        else:    # 만약 음수라면
            break    # 넣지말고 while문 빠져나가기
    total_result.append(temp_result)    # 남은 temp_result는 결과로 total_result에 집어넣기

max_len = 0    # total_result 내 요소 하나하나의 길이를 비교하기 위한 기준 값

for arr in total_result:
    if len(arr) > max_len:    # 만약 길이가 최대값보다 길다면
        max_len = len(arr)    # 최대값은 해당 요소의 길이
        final_result = arr    # 결과는 해당 요소(리스트)

print(max_len)
print(*final_result)