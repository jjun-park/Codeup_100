from sys import stdin

input = stdin.readline

l = int(input().rstrip())
r = int(input().rstrip())

print((l * 2) + (2 * r * 3.141592))      # 양 변(가로)의 길이 + 원의 둘레
