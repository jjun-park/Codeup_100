from sys import stdin
input = stdin.readline

h, w = map(int, input().split())
n = int(input().rstrip())
board = [[0] * w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            board[x-1][y-1+j] = 1   # Y축 이동: 수평
        elif d == 1:
            board[x-1+j][y-1] = 1   # X축 이동: 수직

for k in board:
    print(*k)
#   print(" ".join(map(str, k)))

















