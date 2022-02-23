import sys

input = sys.stdin.readline

N = [int(input().rstrip()) for _ in range(28)]      # 개행, 리스트로 28개 입력받음
absent = [M for M in range(1, 31)]      # 1부터 30번까지의 출석부를 만듬

for i in N:
    absent.remove(i)                # 입력받은 리스트 반복문으로 돌려서 # 출석부에 있는 명단과 대조 후 제거 (remove)

absent.sort(reverse=False)          # 숫자를 오름차순으로 정렬

print(*absent, sep='\n')            # 리스트의 대괄호를 떼고, 개행으로 출력함
