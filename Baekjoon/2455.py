from sys import stdin

input = stdin.readline

customer = [list(map(int, input().split())) for _ in range(0, 4)]

for _ in customer:
    a = customer[0]
    b = customer[1]
    c = customer[2]
    d = customer[3]

A = a[1]-a[0]
B = A + b[1]-b[0]
C = B + c[1]-c[0]
D = C + d[1]-d[0]

print(max(A, B, C, D))