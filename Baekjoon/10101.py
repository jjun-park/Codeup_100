import sys

input = sys.stdin.readline

A, B, C = [int(input()) for _ in range(3)]

if A == B == C:
    print("Equilateral")
elif A+B+C == 180 and (A == B or B == C or A == C):
    print("Isosceles")
elif A+B+C == 180 and (A != B != C):
    print("Scalene")
elif A+B+C != 180:
    print("Error")
