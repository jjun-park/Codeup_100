from sys import stdin

input = stdin.readline

n = int(input().rstrip())

num_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if num_list[i][0] > num_list[i][1] - num_list[i][2]:
        print("do not advertise")
    elif num_list[i][0] == num_list[i][1] - num_list[i][2]:
        print("does not matter")
    elif num_list[i][0] < num_list[i][1] - num_list[i][2]:
        print("advertise")
