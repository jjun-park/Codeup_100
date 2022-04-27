from sys import stdin

input = stdin.readline

n = int(input().rstrip())
num = input().rstrip()
num_list = []

for i in num:
    num_list.append(int(i))

print(sum(num_list))