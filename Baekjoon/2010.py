from sys import stdin

input = stdin.readline

n = int(input().rstrip())
con = [int(input().rstrip()) for _ in range(n)]
power = 0

for i in con:
    power += i

power -= n-1

print(power)