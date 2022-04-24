# 방법 1
numArr = [list(map(int, input().split())) for _ in range(int(input()))]

numArr.sort(key=lambda num: (num[0], num[1]))
# Lambda = 리스트를 오름차순으로 정렬
# 내림차순으로 정렬할 거면 reverse=True 입력

for i in numArr:
    print(i[0], i[1])

# 방법 2
# n = int(input())
# arr = []
# for i in range(n):
#     x, y = map(int, input().split())
#     arr.append((x, y))
#
# arr.sort()
#
# for i in range(n):
#     print(arr[i][0], arr[i][1])