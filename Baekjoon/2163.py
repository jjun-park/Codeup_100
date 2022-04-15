from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

N_split = N-1
M_split = (M-1) * N

print(N_split + M_split)
