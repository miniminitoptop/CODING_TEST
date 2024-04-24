import sys
sys.stdin = open("input.txt","r")

for test_case in range(1,int(input())+1):
    N, K = map(int, input().split())
    lst = list(map(int,input().split()))

    res = 0

    def dfs(i, res):

        global cnt
        if res == K:
            cnt += 1
            return
        elif res > K:
            return
        if i == N:
            return

        dfs(i + 1, res + lst[i])
        dfs(i + 1, res)

    cnt = 0
    dfs(0, 0)

    print(f"#{test_case}",cnt)

