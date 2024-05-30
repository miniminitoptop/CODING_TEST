import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())), reverse=True)
    ans = -1

    for i in range(N):
        for j in range(i+1, N):
            if lst[i]+lst[j] <= M:
                ans = lst[i]+lst[j]
                break
        if ans != -1:
            break

    print(f"#{test_case}", ans)







