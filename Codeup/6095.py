N = int(input().rstrip())
board = [[0] * 19 for _ in range(19)]

for _ in range(N):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

for R in board:
    print(*R)




#
# Baduk = []
# for i in range(20):
#     Baduk.append([])
#     for j in range(20):
#         Baduk[i].append(0)
#
# n = int(input())
#
# for i in range(n):
#     x, y = map(int, input().split())
#     Baduk[x][y] = 1
#
# for i in range(1, 20):
#     for j in range(1, 20):
#         print(Baduk[i][j], end=' ')
#
#     print()








# board = [[0] * 19 for _ in range(19)]
#
# for _ in range(int(input().rstrip())):
#     x, y = map(int, input().split())
#     board[x-1][y-1] = 1
#
# for row in board:
#     print(*row)








# n = int(input())
# arr_2d = [[0 for col in range(19)] for row in range(19)]
#
# for i in range(n):
#     x, y = map(int, input().split())
#     arr_2d[x-1][y-1] = 1
#
# for i in arr_2d:
#     for j in i:
#         print(j, end=" ")
#     print()
