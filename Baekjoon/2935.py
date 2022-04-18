from sys import stdin

input = stdin.readline

A = int(input().rstrip())
N = input().rstrip()
B = int(input().rstrip())

if N == "*":
    print(A * B)
elif N == "+":
    print(A + B)