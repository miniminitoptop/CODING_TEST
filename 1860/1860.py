import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int,input().split()))

    ans = "Possible"
    lst = sorted(lst)

    BB = 0
    cnt = 2
    time = M
    print(lst)
    for i in range(N):

        if lst[i] >= time:
            time = M * (lst[i]//M)
            cnt += 1
            BB += K *

        elif lst[i] <= M:
            ans = "Impossible"
            break

        BB -= 1

        if BB < 0:
            ans = "Impossible"
            break

    print(f"#{test_case}", ans)





