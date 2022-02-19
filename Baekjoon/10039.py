import sys

input = sys.stdin.readline

A, B, C, D, E = (int(input().rstrip()) for _ in range(5))

if A < 40:
    A = 40
if B < 40:
    B = 40
if C < 40:
    C = 40
if D < 40:
    D = 40
if E < 40:
    E = 40

R = int((A + B + C + D + E) / 5)

print(R)
