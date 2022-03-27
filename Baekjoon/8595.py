import sys

input = sys.stdin.readline

cnt = int(input().rstrip())
st = input().rstrip()
str = list(st)
temp = ''
result = 0

for i in st:
    if i >= '0' and i <= '9':
        temp += i
    else:
        if temp:
            result += int(temp)
            temp = ''

if temp:
    e = float(temp)
    result += int(e)

print(result)

##################

# import re
#
# n = input.rstrip()
# string = input.rstrip()
#
# numbers = re.findall("\d+", string)
# numbers = list(map(int, numbers))
#
# print(sum(numbers))