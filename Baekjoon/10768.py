import sys

input = sys.stdin.readline

M = int(input().rstrip())
D = int(input().rstrip())

# if M < 2:
#     print("Before")
#
# if M == 2 and D < 18:
#     print("Before")
# elif M == 2 and D == 18:
#     print("Special")
# elif M == 2 and D > 18:
#     print("After")
#
# if M > 2:
#     print("After")

if M < 2:
    print("Before")
elif M == 2:
    if D < 18:
        print("Before")
    if D == 18:
        print("Special")
    if D > 18:
        print("After")
else:
    print("After")

