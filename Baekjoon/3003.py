Chess = [1, 1, 2, 2, 2, 8]
C_list = list(map(int, input().split()))

for i in range(6):
    print(Chess[i]-C_list[i], end=' ')
