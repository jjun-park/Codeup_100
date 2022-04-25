from sys import stdin

input = stdin.readline

N = list(map(int, input().split()))

print(sum(N[0:]))