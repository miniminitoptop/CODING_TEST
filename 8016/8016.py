import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    ans1 = 2 * N ** 2 - 4 * N + 3
    ans2 = 2 * N ** 2 - 1

    print(f"#{test_case}",ans1, ans2)
