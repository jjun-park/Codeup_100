from sys import stdin

input = stdin.readline

H, M = map(int, input().split())

MM = M - 45

if MM < 0:
    H -= 1
    MM += 60

if H < 0:
    H += 24

print(H, MM)