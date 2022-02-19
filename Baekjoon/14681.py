import sys

input = sys.stdin.readline

X, Y = (int(input().rstrip()) for _ in range(2))  # 개행으로 입력받기

if X > 0 and Y > 0:
    print(1)
elif X < 0 and Y > 0:
    print(2)
elif X < 0 and Y < 0:
    print(3)
elif X > 0 and Y < 0:
    print(4)
