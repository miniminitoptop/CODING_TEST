import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    A , B = map(int,input().split())
    max_cnt = 0
    
    if A > B or B - A == 1 : 
        max_cnt = -1
        print(f'#{test_case} {max_cnt}')
        continue
    
    elif  (B - A) % 2 == 0:
        max_cnt = int((B-A)/2)
        print(f'#{test_case} {max_cnt}')
        continue
    
    else:
        C = B - A
        while C > 0:
            C = C - 3
            print(C)
            max_cnt = max_cnt + 1
            if (C % 2) == 0:
                max_cnt = int(max_cnt + C // 2)
                break
        print(f'#{test_case} {max_cnt}')
        continue
    