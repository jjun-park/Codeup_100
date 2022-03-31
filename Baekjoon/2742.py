from sys import stdin

input = stdin.readline

N = int(input().rstrip())

for i in reversed(range(0, N)):
    print(int(i+1), sep='\n')