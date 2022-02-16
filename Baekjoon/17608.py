import sys

input = sys.stdin.readline

N = int(input().rstrip())
sticks = [int(input().rstrip()) for _ in range(N)]  # 개행으로 리스트값 입력 받음

max_height = 0  # 값을 받기 위해 초기화
cnt = 0     # 값을 받기 위해 초기화
while sticks:   # 리스트 "sticks"를 모두 꺼낼 때까지 반복함
    stick = sticks.pop()    # 리스트 내용 중 가장 마지막 값을 꺼내옴
    if max_height < stick:  # 막대기 값 비교
        cnt += 1            # 조건 성립 시 카운트 +1
        max_height = stick  # max_height 기준을 stick 높이로 설정

print(cnt)

# # Another method to solve this problem

# max_high = sticks[-1]     # 제일 마지막 막대기가 기준점
# cnt = 1   # 제일 마지막 막대기를 카운트에 넣음

# for i in range(N-2, -1, -1):  # 0~4번째 스틱들을 거꾸로 넣음
#     if sticks[i] > max_high:  # 제일 마지막 막대기와 비교
#         max_high = sticks[i]  # 제일 큰 막대기로 치환
#         cnt += 1      # 카운트 +1
#
# print(cnt)
