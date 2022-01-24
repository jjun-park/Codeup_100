n = int(input().rstrip())
for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i, end=' ')

# print(*[i for i in range(1, int(input())+1) if i % 3 != 0])
#
# print(' '.join(map(str, [x for x in range(1, int(input().rstrip()) + 1) if x % 3 != 0])))