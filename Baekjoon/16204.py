import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

A = min(M, K)
B = min(N-M, N-K)

print(A + B)

# 또다른 방법
#
# import sys
#
# input = sys.stdin.readline
#
# N, M, K = map(int, input().split())
#
# count = 0
#
# if M >= K:
#     count += K
# elif M < K:
#     count += M
#
#
# if N-M >= N-K:
#     count += N-K
# else:
#     count += N-M
#
# print(count)
