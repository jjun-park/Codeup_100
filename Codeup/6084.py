h, b, c, s = map(int, input().split())

print(round(h*b*c*s/8/1024/1024, 1), "MB")

# print(숫자, "MB")



# h, b, c, s = map(int, input().split())
#
# size = (h * b * c * s) / 8 / 1024 / 1024
#
# print("%.1f MB" % size)