a, b, c = map(int, input().split())

d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1

print(d)


# import math
# a, b, c = map(int, input().split())
# print(math.lcm(a, b, c))



# a, b, c = map(int, input().split())
#
# # 최대 공약수 —> 최소 공배수 계산할 때 필요
# def getGcd(x, y):
#     while y != 0:
#         temp = x % y
#         x = y
#         y = temp
#     return abs(x)
#
# # 최소 공배수
# def getLcm(x, y):
#     gcdValue = getGcd(x, y)
#     if gcdValue == 0:     # params가 둘 다 0일 때 0을 반환
#         return 0
#     return abs((x * y) / gcdValue)
#
# print(int(getLcm(a, getLcm(b, c))))





# # 70. 더 짧은 GCD 구하기
# def gcd2(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
#
# # 71. 유클리드 호제법 LCM
# def lcm(x, y):
#     return (x * y) // gcd2(x, y)





# people = list(map(int, input().split()))
#
# result = lcm(people[0], people[1])
# print(lcm(result, people[2]))