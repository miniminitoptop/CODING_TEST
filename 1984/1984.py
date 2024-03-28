import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))
    print(f'#{test_case} {int(round((sum(lst)-min(lst)-max(lst))/8))}')
    
 