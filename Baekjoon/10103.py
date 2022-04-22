from sys import stdin

input = stdin.readline

n = int(input().rstrip())
score_ch, score_s = 100, 100

for i in range(n):
    game = list(map(int, input().split()))
    if game[0] > game[1]:
        score_s -= game[0]
    elif game[0] == game[1]:
        continue
    elif game[0] < game[1]:
        score_ch -= game[1]

print(score_ch, score_s, sep='\n')
