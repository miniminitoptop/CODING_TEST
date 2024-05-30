import sys
sys.stdin = open("input.txt", "r")

def dfs(c,v):
    global ans

    ans = max(ans, len(v))

    for n in lst[c]:
        if n not in v:
            dfs(n, v+[n])

for test_case in range(1,int(input())+1):

    N, M = map(int, input().split())

    lst = [[] for _ in range(N+1)]

    for i in range(M):
        X, Y = map(int, input().split())

        lst[X].append(Y)
        lst[Y].append(X)

    ans = 0

    for s in range(1, N+1):
        dfs(s, [s])

    print(f"#{test_case}", ans)






