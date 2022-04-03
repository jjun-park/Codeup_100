from sys import stdin

input = stdin.readline

N = int(input().rstrip())
students = [list(map(int, input().split())) for _ in range(N)]
apple_remain = []

for i in range(0, N):
    apple = students[i][1] % students[i][0]
    apple_remain.append(apple)

print(sum(apple_remain))

# 01을 00으로 나눈 나머지를 변수로 지정
# 다시 00 + 나눈 나머지들을 모두 더해서 프린트


#################


# 두일이가 푸는 방법

# n = int(input())
#
# result = 0
# for _ in range(n):
#     a, b = map(int, input().split())
#     result += b % a
#
# print(result)