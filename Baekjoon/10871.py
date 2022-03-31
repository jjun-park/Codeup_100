from sys import stdin

input = stdin.readline

N, X = map(int, input().split())
num = input().split()
num_list = []

for i in range(0, N):
    if int(num[i]) < X:
        num_list.append(num[i])

print(*num_list)