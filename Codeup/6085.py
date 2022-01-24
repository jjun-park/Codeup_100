w, h, b = map(int, input().split())
m = w*h*b/8/1024/1024
print(f'{m:.2f}', "MB")


# w,h,b = map(int, input().split())
# result = w*h*b/1024/1024/8
#
# print(f'{result:.2f} MB')
