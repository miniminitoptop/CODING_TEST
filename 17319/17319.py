import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = input()
    if N % 2 == 0:
        if a[0:int(N/2)] == a[int(N/2):]:
            print(f"#{test_case} YES")
        else:
            print(f"#{test_case} NO")
    else:
        print(f"#{test_case} NO")
