from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

if M <= 2:
    print("NEWBIE!")
elif 2 < M <= N:
    print("OLDBIE!")
else:
    print("TLE!")

# 뉴비: 1, 2학년
# 올드비: N 이하, 뉴비 아님
# TLE : 뉴비도 아니고 올드비도 아니고