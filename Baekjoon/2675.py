from sys import stdin

input = stdin.readline

T = int(input().rstrip())

for _ in range(T):  # T번 입력을 받기 위해 반복문 사용
    R, S = input().split()  # 공백을 기준으로 입력을 받음
    text = ''  # 각 문자마다 반복시켜 밀어넣을 공간을 설정
    for i in S:  # 문자열 내 각각의 인수를 입력하기 위해 반복문 사용
        text += i * int(R)  # 입력된 인수를 R번 반복해서 변수에 밀어 넣음

    print(text)
