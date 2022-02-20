import sys

input = sys.stdin.readline

K, N, M = map(int, input().split())
Money = (K * N) - M

if Money < 0:
    Money = int(0)

print(Money)
