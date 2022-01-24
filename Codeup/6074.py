z = ord(input())
x = ord('a')

while x <= z:
    print(chr(x), end=' ')
    x += 1

# a = input()
# alp = ord('a')  # ord('a')는 유니코드 97
# while True:
#     print(chr(alp), end=' ')  # chr(97)은 알파벳 a
#
#     if chr(alp) == a:
#         break
#
#     alp = alp + 1

# for s in range(ord('a'), ord(input().rstrip()) + 1):
#     print(chr(s), end=' ')
