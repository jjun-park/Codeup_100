from sys import stdin

input = stdin.readline

n = int(input().rstrip())
question = map(int, input().split())
total, score = 0, 1

for q in question:
    if q == 1:
        total += score
        score += 1
    elif q == 0:
        score = 1

print(total)