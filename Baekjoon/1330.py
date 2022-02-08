from sys import stdin

input = stdin.readline

A, B = map(int, input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")
