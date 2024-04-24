import sys
sys.stdin = open("input.txt","r")

def dfs(n, T ,K):
    global ans

    if K > L:
        return

    ans = max(ans, T)

    if n == N:
        return
    
    dfs(n+1, T + T_lst[n], K + K_lst[n])
    dfs(n+1, T, K)


for test_case in range(1, int(input())+1):
    N, L = map(int, input().split())
    T_lst = []
    K_lst = []

    for i in range(N):
        T, K = map(int, input().split())
        T_lst.append(T)
        K_lst.append(K)

    ans = 0

    dfs(0,0,0)

    print(f"#{test_case}",ans)


# DFS
