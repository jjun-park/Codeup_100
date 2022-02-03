from itertools import combinations
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
Max = int(1e9)

for a, b, c in combinations(cards, 3):
    output = a + b + c
    if output <= M and abs(M - output) < Max:
        Max = abs(M - output)

print(M - Max)
