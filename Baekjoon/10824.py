from sys import stdin

input = stdin.readline

number = list(map(str, input().split()))

A = number[0] + number[1]
B = number[2] + number[3]

print(int(A) + int(B))