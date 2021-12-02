h, w = map(int, input().split())
n = int(input().rstrip())
board = [[0] * w for _ in range(h)]
Xst = []

for i in range(n):
    Xst.append(list(map(int, input().split())))

for x_one in Xst:
    l, d, x, y = x_one
    if d == 0:
        for j in range(l):
            board[x-1][y-1+j] = 1
    elif d == 1:
        for j in range(l):
            board[x-1+j][y-1] = 1

for k in board:
    print(*k)
