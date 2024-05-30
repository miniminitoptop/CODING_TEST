import sys
sys.stdin = open("input.txt","r")

def fun(n, m):
    global ans

    m += 1
    ans *= n

    if m == M:
        return

    fun(n, m)


for test_case in range(1, 11):
    S = int(input())
    N, M = map(int, input().split())

    ans = 1

    fun(N, 0)

    print(f"#{S}", ans)

