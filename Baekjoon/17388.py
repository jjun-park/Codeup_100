import sys

input = sys.stdin.readline

S, K, H = list(map(int, input().split()))
Camp = S + K + H
Camp_2 = {S, K, H}

if Camp >= 100:
    print("OK")
elif Camp < 100:
    Camp_2 = {S: "Soongsil", K: "Korea", H: "Hanyang"}
    print(Camp_2.get(min(Camp_2)))
