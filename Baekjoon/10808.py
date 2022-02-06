# from sys import stdin
#
# input = stdin.readline
#
# string = list(input())
# alphabets = []
#
# for _ in range(26):
#     alphabets.append(0)
#
# for i in string:
#     alphabets[ord(i) - 97] += 1
#
# for j in alphabets:
#     print(j, end='')

import sys
import string

input = sys.stdin.readline

S = list(input().rstrip())
alpha_dict = dict.fromkeys(string.ascii_lowercase, 0)

for q in S:
    alpha_dict[q] += 1

print(*alpha_dict.values())
