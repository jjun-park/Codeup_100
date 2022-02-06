from sys import stdin
input = stdin.readline

N = int(input().rstrip())
print(int(N - (N * 0.22)), int(N - (N * 0.2 * 0.22)))
