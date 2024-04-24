import sys
sys.stdin = open("input.txt", "r")

def dfs(n):
    global ans

    if n == N:
        ans = max(ans, int("".join(map(str, lst))))
        return


    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str, lst)))

            if (n, chk) not in v:
                dfs(n + 1)

                v.append((n, chk))

            lst[j], lst[i] = lst[i], lst[j]

T = int(input())

for test_case in range(1, T + 1):
    M, N = input().split()
    N = int(N)

    lst, v = [], []

    L = len(M)

    ans = 0

    for i in M:
        lst.append(i)
    dfs(0)


    print(f'#{test_case} {ans}')







    