s = int(input().rstrip())
n, m = 0, 0
while True:
    n += m
    m += 1
    if n >= s:
        break

print(n)