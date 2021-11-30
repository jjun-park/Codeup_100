N = int(input())
n_list = list(map(int, input().split()))
d = [0] * 23

for i in n_list:
    d[i-1] += 1

print(' '.join(map(str, d)))