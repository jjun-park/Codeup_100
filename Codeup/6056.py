a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# a, b = map(int, input().split())
# if bool(a) != bool(b):
#    print("True")
# else:
#    print("False")

# bool1, bool2 = map(bool, map(int, input().split()))
# print(bool1 != bool2)

# a, b = map(int, input().split())
# print(True if bool(a) ^ bool(b) else False)
