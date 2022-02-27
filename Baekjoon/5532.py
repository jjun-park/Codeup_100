import sys

input = sys.stdin.readline

L, A, B, C, D = [int(input().rstrip()) for _ in range(5)]

Day_K = A // C
if A % C != 0:
    Day_K += 1

Day_M = B // D
if B % D != 0:
    Day_M += 1

if Day_M >= Day_K:
    print(L - Day_M)

if Day_M < Day_K:
    print(L - Day_K)
