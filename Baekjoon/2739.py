import sys

input = sys.stdin.readline

N = int(input().rstrip())

for i in range(1, 10):
    print(N, '*', i, '=', N * i)
