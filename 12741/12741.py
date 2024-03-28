import sys
sys.stdin = open("input.txt", "r")

T = int(input())
lst = []
for test_case in range (1,T+1):
    A, B, C, D = map(int,input().split())
    lst.append(f'#{test_case} {max(min(B,D) - max(A,C),0)}')
for i in lst:
    print(i)