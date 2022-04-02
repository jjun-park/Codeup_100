from sys import stdin

input = stdin.readline

temp = []

while True:
    a, b = map(int, input().split())
    if a == 0 & b == 0:
        break
    temp.append((a+b))

for i in temp:
    print(i)