from sys import stdin

input = stdin.readline

N = int(input().rstrip())

for i in range(N):
    print(int(i+1), sep='\n')