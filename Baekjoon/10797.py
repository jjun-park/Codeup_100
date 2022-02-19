import sys

input = sys.stdin.readline

Day = int(input().rstrip())
Car = list(map(int, input().split()))
Count = 0

for i in Car:
    if i == Day:
        Count += 1

print(Count)


# Another Method to Solve (두일팟)

# day = int(input().rstrip())
# car_num = list(man(int, input().split()))
# print(car_num.count(day))