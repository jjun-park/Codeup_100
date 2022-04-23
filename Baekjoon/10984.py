from sys import stdin

input = stdin.readline

N = int(input().rstrip())
shape = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    result = shape[i][1] - shape[i][0] + 2
    print(result)