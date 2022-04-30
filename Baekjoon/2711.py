from sys import stdin

input = stdin.readline

n = int(input().rstrip())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = list(b)
    del b[a-1]
    b_str = "".join(b)    # "".join(리스트) : 리스트를 문자로 출력
    print(b_str)
