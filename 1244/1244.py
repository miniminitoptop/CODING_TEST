import sys
sys.stdin = open("input.txt", "r")

def dfs(n):
    global ans
    if n == N:
        ans = max(ans,int("".join(map(str,lst))))
        return

    for i in range(L-1):
        print(i)
        for j in range (i+1,L):
            print(j)
            lst[i], lst[j] = lst[j], lst[i]
            dfs(n+1)
            lst[j], lst[j] = lst[i], lst[j]


T = int(input())

for test_case in range(1, T + 1):
    M, N = input().split()
    N = int(N)
    lst = list(map(int, M))
    print(lst)

    L = len(lst)
    print(L)

    ans = 0
    dfs(0)
    print(f'#{test_case} {ans}')


    