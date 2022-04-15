from sys import stdin

input = stdin.readline

lists = []
count = 0

while True:
    n, m = map(int, input().split())
    lists.append([n, m])
    count += 1
    if n == 0 & m == 0:
        break

lists.pop()

for i in range(0, count-1):
    if lists[i][0] > lists[i][1]:
        print("Yes")
    else:
        print("No")
