from sys import stdin

input = stdin.readline

h, m = map(int, input().split())
n = int(input().rstrip())

h += n // 60
m += n % 60
if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)
