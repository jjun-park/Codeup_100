from sys import stdin
from itertools import combinations

input = stdin.readline
dwarf = [int(input().rstrip()) for _ in range(9)]

for i in combinations(dwarf, 7):
    if sum(i) == 100:
        dwarfs = list(map(int, i))  # 변수를 리스트로 나타내고 싶을 때
        dwarfs.sort()   # reverse = True 넣으면 내림차순으로
        for j in dwarfs:
            print(j)
        break
