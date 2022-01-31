# from itertools import combinations
# from sys import stdin
# input = stdin.readline
#
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# minus = int(1e9)    # 무한대수
#
# for a, b, c in combinations(cards, 3):  # 리스트, 추출할 수
#     temp = a + b + c
#     if temp <= M and abs(M - temp) < minus:
#         minus = abs(M - temp)  # minus 갱신
#
# print(M - minus)


from itertools import combinations
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
Max = int(1e9)

for a, b, c in combinations(cards, 3):
    output = a + b + c
    if output <= M and abs(M - output) < Max:
        Max = abs(M - output)

print(M - Max)
