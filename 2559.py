N, K = map(int, input().split())
temperature = list(map(int, input().split()))

# temperature의 원소에 대해 연속된 K개의 숫자를 별도의 리스트로 만들고 합 구하기

maximum = (-100)*100000    # 주어진 문제가 가질 수 있는 가장 최솟값으로 maximum의 기본값 설정

# 시간 복잡도를 줄이기 위해서 처음 K개의 합을 구하고 그 이후에는 뒤의 원소를 더하고 맨 앞의 원소를 빼는 식으로 다음 합을 구하는 방법을 쓴다.
# 매번 5개씩 묶어서 리스트를 지정하는 것보다 훨씬 시간복잡도가 적어진다.
# 이것도 chatGPT가 알려줬다...

init_sum = 0    # 처음 K개의 합을 담는 변수
for i in range(K):
    init_sum += temperature[i]

if init_sum > maximum:
    maximum = init_sum

for i in range(N-K):
    temp_sum = init_sum + temperature[i+K] - temperature[i]
    # 앞에 있는 숫자는 빼주고 한 칸 뒤에 오는 숫자는 더해주고 하면서 5개씩 묶음을 바꾸기
    if temp_sum > maximum:    # 만약 기존 최댓값보다 더 큰 값이라면
        maximum = temp_sum    # 새로운 최댓값으로 설정
    init_sum = temp_sum    # temp_sum을 init_sum으로 바꾸고 다시 계산

print(maximum)