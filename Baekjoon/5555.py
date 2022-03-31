ring_string = input().rstrip()

N = int(input().rstrip())
count = 0  # 변수 초기화

for _ in range(N):
    ring = input().rstrip()
    ring += ring    # 문자열 1개를 한번 더 복붙해서 서로 잇는다.

    if ring.find(ring_string) != -1:    # 문자열 포함하지 않는다 = -1로 반환
        count += 1

print(count)


##############


import re
import sys

input = sys.stdin.readline

'''
    [요약]
    1. 반지는 대문자 10개 
    2. 문자열을 포함하는 반지는 몇 개 인지?

    [풀이]
    1. 입력 후 리스트 합치고 정규표현식 추출 

    [주의점]

'''

cnt = 0
p = re.compile(input().rstrip())
for _ in range(int(input().rstrip())):
    ring = input().rstrip()
    ring += ring

    if re.search(p, ring) is not None:  # is not None = Null
        cnt += 1

print(cnt)