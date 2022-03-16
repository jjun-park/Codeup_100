from sys import stdin

input = stdin.readline

score = [int(input().rstrip()) for _ in range(20)]

'''
 W대학 => score[0:10]  -> score[:10] (0 to 9)
 K대학 => score[10:19]  -> score[10:] (10 to 19)
'''

# W대학의 상위 3개 스코어
w_score = sum(sorted(score[:10], reverse=True)[:3])    # 슬라이서 사용 (0 to 2까지만 데이터 자름)
# K대학의 상위 3개 스코어
k_score = sum(sorted(score[10:], reverse=True)[:3])    # 슬라이서 사용 (0 to 2까지만 데이터 자름)

print(w_score, k_score)