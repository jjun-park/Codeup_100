from sys import stdin
input = stdin.readline

L = int(input().rstrip())
T = L // 5

if L % 5 != 0:
    T += 1

print(T)
