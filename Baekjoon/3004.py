from sys import stdin
input = stdin.readline

N = int(input().rstrip())

row = 1
col = 1

for i in range(N):
    row += col
    if i % 2 == 0:
        col += 1

print(row)
