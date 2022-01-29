from sys import stdin
input = stdin.readline

N, W, H = map(int, input().split())
D = ((W ** 2) + (H ** 2)) ** 0.5
Answer = []

for i in range(N):
    stick = int(input())
    if W >= stick or H >= stick:
        Answer.append("DA")
    elif D >= stick:
        Answer.append("DA")
    else:
        Answer.append("NE")

for j in Answer:
    print(j)
