dwarves = []
for _ in range(9):
    dwarves.append(int(input()))    # 난쟁이들의 키를 요소로 갖는 리스트 생성

# 9명 중 빼고 계산할 2명을 정하고 실제로 계산하는 과정
for i in range(8):
    for j in range(i+1, 9):
        temp_dwarves = dwarves[:]    # dwarves의 복사본을 준비해주고
        temp_dwarves[i] = 0
        temp_dwarves[j] = 0    # 고려하지 않을 것이기 때문에 0으로 만들어 준 다음
        if sum(temp_dwarves) == 100:
            result = temp_dwarves
            break    # 하나 찾으면 그냥 더 찾지 말고 빠져나오기

# 오름차순으로 정렬
result.sort()

for i in range(2, 9):    # 앞의 2개는 고려하지 않은 0이기 때문에 2부터 시작
    print(result[i])    # 하나씩 출력해주기