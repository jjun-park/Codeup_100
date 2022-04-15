from sys import stdin

input = stdin.readline

t = int(input().rstrip())
sum = [list(map(int, input().split())) for _ in range(t)]

for i in range(1, t+1):
    a = sum[i-1][0]
    b = sum[i-1][1]
    sums = a + b
    print(f'Case #{i}:', sum[i-1][0], "+", sum[i-1][1], "=", sums)