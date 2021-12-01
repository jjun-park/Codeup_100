N = int(input().rstrip())
board = [[0] * 19 for _ in range(19)]

for _ in range(N):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

for R in board:
    print(*R)
