from sys import stdin

input = stdin.readline

A, B, C, D, E = (int(input().rstrip()) for _ in range(5))
sec = 0

while True:
    if A < 0:
        sec += C
        A += 1
        continue
    if A == 0:
        sec += D
        sec += E
        A += 1
        continue
    if A > 0:
        sec += E
        A += 1
    if A == B:
        break

print(sec)