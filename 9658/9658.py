import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    N = input()

    M = len(N) - 1

    N = round(int(N)/(10**M), 1)

    K = len(str(int(N)))

    if K == 2:
        N /= 10
        M += 1

    print(f"#{test_case} {N}*10^{M}")
