from sys import stdin
input = stdin.readline

A, B = map(int, input().split())
N = B
output = N - A

print(output, B)
