L, P = map(int, input().split())
PP = L * P

News = list(map(int, input().split()))

for i in News:
    print(i - PP, end=' ')
