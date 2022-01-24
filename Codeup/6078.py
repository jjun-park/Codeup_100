# while True:
#     x = str(input())
#     print(x)
#     if x == 'q':
#         break


arr = []
char = ''

while 1:
    char = input()
    arr.append(char)

    if char == 'q':
        break

for arr_char in arr:
    print(arr_char)
