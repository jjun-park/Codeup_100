from sys import stdin

input = stdin.readline

A, B, C, D = map(int, input().split())
Team = [A, B, C, D]
Team.sort()

first_T = Team[0] + Team[3]
second_T = Team[1] + Team[2]

print(abs(first_T - second_T))
