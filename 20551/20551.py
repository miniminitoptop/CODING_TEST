import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int,input().split())

    if C < 3 or B < 2:
        print(f"#{test_case} -1")
        continue

    A1 = min(C - 2,A)
    B1 = min(C - 1,B)
    N = A-A1+B-B1

    print(f"#{test_case} {N}")
