import sys
input = sys.stdin.readline

game = [list(map(int, input().split())) for _ in range(19)]
num = int(input().rstrip())

for i in range(num):
    x, y = map(int, input().split())
    for j in range(19):
        game[x - 1][j] = (1 if game[x - 1][j] == 0 else 0)
        game[j][y - 1] = (1 if game[j][y - 1] == 0 else 0)

for k in game:
    print(*k)
#   print(" ".join(map(str, k)))








# Baduk = []
#
# for i in range(19):
#     Baduk.append([])
#     for j in range(19):
#         Baduk[i].append(0)
#
# for i in range(19):
#     Baduk[i] = list(map(int, input().split()))
#
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#
#     for j in range(19):
#         if Baduk[x-1][j] == 0:
#             Baduk[x-1][j] = 1
#         else:
#             Baduk[x-1][j] = 0
#
#         if Baduk[j][y-1] == 0:
#             Baduk[j][y-1] = 1
#         else:
#             Baduk[j][y-1] = 0
#
# for i in range(19):
#     for j in range(19):
#         print(Baduk[i][j], end= ' ')
#     print()









# board = [list(map(int, input().split())) for _ in range(19)]
#
# for _ in range(int(input().rstrip())):
#     x, y = map(int, input().split())
#
#     for i in range(19):
#         board[x-1][i] = int(not (bool(board[x-1][i])))
#         board[i][y-1] = int(not (bool(board[i][y-1])))  # 0 = 거짓 / 1 = 참
#
# for row in board:
#     print(*row)










# arr_2d = [[0 for col in range(19)] for row in range(19)]
#
# for i in range(19):
#     arr_2d[i] = list(map(int, input().split()))
#
# n = int(input())
#
# for i in range(n):
#     x, y = map(int, input().split())
#     for j in range(19):
#         arr_2d[j][y-1] = 1 if arr_2d[j][y-1] == 0 else 0
#         arr_2d[x-1][j] = 1 if arr_2d[x-1][j] == 0 else 0
#
# for i in arr_2d:
#     for j in i:
#         print(j, end=" ")
#     print()