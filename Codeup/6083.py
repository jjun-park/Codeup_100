r, g, b = map(int, input().rstrip().split())

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)

print(r * g * b)




# r, g, b = map(int, input().split())
# total = 0
#
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print("%d %d %d" % (i, j, k))
#             total += 1
#
# print(total)
