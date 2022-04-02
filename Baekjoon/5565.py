from sys import stdin

input = stdin.readline

total = int(input().rstrip())
book = [int(input().rstrip()) for _ in range(9)]

one = total - sum(book)

print(one)