import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    lst = list(int(input()) for _ in range(N))

    ans = 0

    for i in lst:
        ans += max(int(sum(lst)/N), i) - min(int(sum(lst)/N), i)

    print(f"#{test_case}", ans//2)

