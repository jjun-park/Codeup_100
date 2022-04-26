from sys import stdin

input = stdin.readline

n = int(input().rstrip())
k = [int(input().rstrip()) for _ in range(n)]

for i in k:
    print("=" * i)