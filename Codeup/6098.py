from sys import stdin
input = stdin.readline

board = [[] * 10 for _ in range(10)]

for i in range(10):
    board[i] = list(map(int, input().split()))

x = 1
y = 1

while True:
    if board[x][y] == 0:        # 갈 수 있는 곳
        board[x][y] = 9
    elif board[x][y] == 2:      # 먹이가 있는 곳
        board[x][y] = 9
        break

    if board[x][y+1] != 1:      # 개미의 이동-수평
        y += 1
    elif board[x+1][y] != 1:    # 개미의 이동-수직
        x += 1

    if board[x][y+1] == 1 and board[x+1][y] == 1:       # 장애물이 있는 곳
        break

    if x == 9 and y == 9:   # 이미 지나간 길
        break

for j in board:
    print(" ".join(map(str, j)))

'''
X축 이동: 수직 / Y축 이동: 수평
'''

# while True:
#     if board[x][y] == 2:
#         board[x][y] = 9
#         break
#     if board[x][y + 1] != 1:
#         board[x][y] = 9
#         y += 1
#     else:
#         if board[x + 1][y] != 1:
#             board[x][y] = 9
#             x += 1
#         else:
#             board[x][y] = 9
#             break
#
# for j in range(10):
#     for k in range(10):
#         print(board[j][k], end=' ')
#     print()

