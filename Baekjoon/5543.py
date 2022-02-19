import sys

input = sys.stdin.readline

A, B, C, D, E = (int(input().rstrip()) for _ in range(5))

print(min(A + D, A + E, B + D, B + E, C + D, C + E) - 50)
