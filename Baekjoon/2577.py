from sys import stdin

input = stdin.readline

A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())

mul = A * B * C
mul_list = list(map(int, str(mul)))     # int를 list로 바꾸는 방법

for i in range(0, 10):
    print(mul_list.count(i))    # for문 돌려서, 카운트 하고 싶은 특정 값을 순서대로 넣음
