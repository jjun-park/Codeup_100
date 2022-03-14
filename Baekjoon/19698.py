from sys import stdin

input = stdin.readline

N, W, H, L = map(int, input().split())

W_L = W // L
H_L = H // L
max_N = W_L * H_L

if max_N >= N:
    print(N)
else:
    print(max_N)
