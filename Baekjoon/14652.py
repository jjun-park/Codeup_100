from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())

print(*divmod(K, M))
# print(K // M, K % M)


# A = [[0] * M for _ in range(N)]
# temp = 0
#
# for i in range(N):
#     for j in range(M):
#         A[i][j] = temp
#         if temp == 6:
#             print(i, j)
#             exit(0)
#         temp += 1
