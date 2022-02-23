import sys

input = sys.stdin.readline

gan_arr = list(range(10))
zi_arr = [i for i in "ABCDEFGHIJKL"]

year = int(input().rstrip())

gan_str = gan_arr[(year % 10) - 4]      # 2014: 갑오(G0)
zi_str = zi_arr[(year % 12) - 4]        # 갑의 인덱스를 0으로 반환하려면, year에서 -4를 해줘야함

print(zi_str, gan_str, sep='')
