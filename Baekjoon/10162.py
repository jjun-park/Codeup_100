import sys

input = sys.stdin.readline

N = int(input().rstrip())

A = 0
B = 0
C = 0

if N >= 300:
    A += N // 300
    N %= 300
if 60 <= N <= 299:
    B += N // 60
    N %= 60
if N < 60:
    C += N // 10
    N %= 10

if N == 0:
    print(A, B, C)
if N != 0:
    print(-1)
