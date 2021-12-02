game = [list(map(int, input().split())) for _ in range(19)]
num = int(input().rstrip())

for i in range(num):
  a, b = map(int, input().split())
  for j in range(19):
    game[a-1][j] = (1 if game[a-1][j] == 0 else 0)
    game[j][b-1] = (1 if game[j][b-1] == 0 else 0)

for i in game:
  print(*i)
