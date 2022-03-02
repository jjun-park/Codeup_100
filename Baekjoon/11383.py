import sys

input = sys.stdin.readline

N, M = map(int, input().split())

firImg = [input().rstrip() for _ in range(N)]        # 돌돔 사진     # ABCDE
secImg = [input().rstrip() for _ in range(N)]        # 됾 사진      # AABBCCDDEE

Check = True

for i in range(N):
    ref = ""        # 검증 기준이 되는 리스트 값을 받기 위해 공백으로 설정함
    for j in firImg[i]:     # firImg의 0번째 값: ABCDE -> 반복문 돌리게 되면 리스트값이 A, B, C, D, E로 쪼개져 들어감
        ref += j * 2

    if ref != secImg[i]:    # secImg 리스트의 0번째 값: AABBCCDDEE
        Check = False
        break

print("Eyfa" if Check else "Not Eyfa")      # True값 "if" 조건문 "else" False값
