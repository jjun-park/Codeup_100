from sys import stdin

input = stdin.readline

t = int(input().rstrip())
sum = [list(map(int, input().split())) for _ in range(t)]

for i in range(0, t):
    A = sum[i][0]
    B = sum[i][1]
    print(A + B)