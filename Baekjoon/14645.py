from sys import stdin
input = stdin.readline


N, K = map(int, input().split())    # N = 정거장 수, K = 출발역 탑승 인원

for _ in range(N):
    A, B = map(int, input().split())

print("비와이")
