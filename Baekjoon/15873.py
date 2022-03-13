from sys import stdin

input = stdin.readline

N = input().rstrip()    # string으로 받아야 리스트로 분할 가능

if N[1] == '0':         # 계산할 때는 string -> int로 변환 필수
    print(int(10) + int(N[2:]))
else:
    print(int(N[0]) + int(N[1:]))
