from sys import(stdin)

input = stdin.readline

n = int(input().rstrip())

for i in range(n):
    n_list = list(input().rstrip())
    print(n_list[0] + n_list[-1])