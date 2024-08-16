N = int(input())    # 붙인 색종이의 개수
papers = [list(map(int, input().split())) for _ in range(N)]
area = set()    # 색종이의 넓이를 담을 변수
# white_paper = [[0]*100 for _ in range(100)]

for paper in papers:    # 각 종이가 차지하는 영역을 격자로 생각해서 set에 넣기
    i = 99-paper[1]
    j = paper[0]
    for i in range(99-paper[1], 89-paper[1], -1):
        for j in range(paper[0], paper[0]+10):
            area.add((i, j))

# 이렇게 하면 중복된 부분은 제외하고 생각할 수 있다.
# 다른 색종이 문제랑 똑같이 풀었는데 오래 걸릴 것 같긴 하다...
# 오래 안 걸렸다!

print(len(area))