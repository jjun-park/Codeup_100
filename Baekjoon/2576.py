from sys import stdin

input = stdin.readline

N = [int(input().rstrip()) for _ in range(7)]
odd = []

for i in N:
    if i % 2 != 0:
        odd.append(i)

if sum(odd) != 0:
    print(sum(odd))
    print(min(odd))
elif sum(odd) == 0:
    print(-1)
