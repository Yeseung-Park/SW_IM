N, M = map(int, input().split())    # 가로와 세로의 길이
num_of_line = int(input())
line_arr = [list(map(int, input().split())) for _ in range(num_of_line)]
paper = [[0]*N for _ in range(M)]

# for line in line_arr:
#     if line[0] == 0:
#         for i in range(line[1]):
#             for j in range(N):
#                 paper[i][j] = 'W'
#         for i in range(line[1], M):
#             for j in range(N):
#                 paper[i][j] = 'X'
#     elif line[0] == 1:
#         for i in range(M):
#             for j in range(line[1]):
#                 paper[i][j] = 'Y'
#         for i in range(M):
#             for j in range(line[1], N):
#                 paper[i][j] = 'Z'

print(line_arr)
print(paper)