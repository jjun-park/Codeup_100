a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not a and not b)

bool1, bool2 = map(bool, map(int, input().split()))
print(not (bool1 or bool2))
