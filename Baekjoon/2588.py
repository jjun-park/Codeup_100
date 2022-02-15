from sys import stdin

input = stdin.readline

A = int(input().rstrip())
B = int(input().rstrip())
B_list = list(map(int, str(B)))

for i in reversed(range(0, 3)):
    R = A * B_list[i]
    print(R)

print(A * B)



# 노가다 무지성으로 풀기

# A_list = list(map(int, str(A))) -> 추가하기

# C_1 = A_list[2] * B_list[2]
# C_2 = (A_list[1] * B_list[2]) * 10
# C_3 = (A_list[0] * B_list[2]) * 100
# C = int(C_1 + C_2 + C_3)
#
# D_1 = A_list[2] * B_list[1]
# D_2 = (A_list[1] * B_list[1]) * 10
# D_3 = (A_list[0] * B_list[1]) * 100
# D = int(D_1 + D_2 + D_3)
#
# E_1 = A_list[2] * B_list[0]
# E_2 = (A_list[1] * B_list[0]) * 10
# E_3 = (A_list[0] * B_list[0]) * 100
# E = int(E_1 + E_2 + E_3)
#
# print(C)
# print(D)
# print(E)
# print(C + D * 10 + E * 100)



# 도일이 계산식

# p = int(input())
# q = input()
#
# w = p * int(q[2])
# x = p * int(q[1])
# y = p * int(q[0])
# z = p * int(q)
#
# print(w, x, y, z, sep="\n")