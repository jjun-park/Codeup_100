from sys import stdin
input = stdin.readline

# a = list(map(int, input().split()))
# c = list(map(int, input().split()))
# b = [c[0]-a[2], c[1]//a[1], c[2]-a[0]]
# print(*b)

A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = []

B.append(C[0]-A[2])
B.append(C[1]//A[1])
B.append(C[2]-A[0])

print(*B)