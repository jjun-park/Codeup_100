import sys

input = sys.stdin.readline

N, M = map(int, input().split())

if N <= M:
    print(1)
elif N > M:
    print(0)
