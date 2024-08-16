N = int(input())    # N: 학생들의 수
numbers = list(map(int, input().split()))
order = []    # 학생들의 순서를 담는 리스트

# insert를 잘 기억하고 사용하자!
# list.insert(index, element): list에 index에 element 추가

for i in range(N):
    if numbers[i] == 0:    # i번째 학생이 가지고 있는 숫자가 0일 경우
        order.append(i+1)    # 그냥 맨 뒤에 그대로 서기
    else:    # 그 외의 경우
        order.insert(i-numbers[i], i+1)
        # 자기가 서 있던 위치에서 가지고 있던 숫자만큼 앞으로 가기

print(*order)