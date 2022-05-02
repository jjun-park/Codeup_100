from sys import stdin

input = stdin.readline

name = list(input().split("-"))

for i in name:
    print(i[0], end="")