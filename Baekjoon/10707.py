import sys

input = sys.stdin.readline

A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())
D = int(input().rstrip())
P = int(input().rstrip())

X_Corp = P * A
Y_Corp = 0

if P < C:
    Y_Corp = B
elif P >= C:
    Y_Corp = ((P-C) * D) + B

if X_Corp >= Y_Corp:
    print(Y_Corp)
else:
    print(X_Corp)
