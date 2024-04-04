import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    A , B = map(int,input().split())
    max_cnt = 0
    
    if A > B or B - A == 1:
        max_cnt = -1
        print(f'#{test_case} {max_cnt}')
        continue
    
    elif (B - A) % 2 == 0:
        max_cnt = int((B-A)/2)
        print(f'#{test_case} {max_cnt}')
        continue
    
    elif (B - A) % 2 == 1:
        max_cnt = (B - A - 3) // 2 + 1
        print(f'#{test_case} {max_cnt}')
        continue
    