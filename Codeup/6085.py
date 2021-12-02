w, h, b = map(int, input().split())
m = w*h*b/8/1024/1024
print(f'{m:.2f}', "MB")
