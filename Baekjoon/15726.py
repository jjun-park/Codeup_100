from sys import stdin

input = stdin.readline

A, B, C = map(int, input().split())

Carc_1 = int(A * B / C)
Carc_2 = int(A / B * C)

if Carc_1 < Carc_2:
    print(Carc_2)
else:
    print(Carc_1)
