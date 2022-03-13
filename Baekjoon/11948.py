from sys import stdin
from itertools import combinations

input = stdin.readline

A, B, C, D, E, F = (int(input().rstrip()) for _ in range(6))

Sci = [A, B, C, D]
His = [E, F]

His_M = max(His)
Max_Sci_S = -1         # 비교값 기준 설정 (점수는 마이너스가 안 나오니까)

for i in combinations(Sci, 3):
    Sci_S = sum(i)
    Max_Sci_S = max(Sci_S, Max_Sci_S)       # Max를 쓰려면 괄호 안에 비교인자를 2개 이상 써야 한다.

print(Max_Sci_S + His_M)
