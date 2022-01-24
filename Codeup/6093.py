n = int(input())
k = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(k[i], end=' ')



# n = int(input())
# a = list(reversed(list(map(int, input().split()))))
#
# for i in range(n):
#     print(a[i], end=' ')





# n = int(input())
# num_list = input().split()
#
# num_list.reverse()
#
# for i in range(n):
#     print(num_list[i], end=' ')




# n = int(input())
# print(" ".join(repr(i) for i in reversed(list(map(int, input().split())))))




# input().rstrip()
# print(*list(map(int, input().split()))[::-1])
