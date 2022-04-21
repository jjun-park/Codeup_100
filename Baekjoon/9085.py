from sys import stdin

input = stdin.readline

T = int(input().rstrip())
lists = []

for _ in range(T):
    N = int(input().rstrip())
    series = list(map(int, input().split()))
    lists.append(series)

for i in range(T):
    print(sum(lists[i]))