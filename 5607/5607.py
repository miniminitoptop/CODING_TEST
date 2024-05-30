import sys
sys.stdin = open("input.txt", "r")

def fun(n,r,s):

    global res1
    global res2

    if n == s:
        return

    if r == 0:
        r = 1

    res1 *= n
    res2 *= r

    fun(n-1, r-1, s)

T = int(input())

for test_case in range(1, T+1):
    N, R = map(int, input().split())

    # res1, res2 = 1, 1
    #
    # if N-R > R:
    #     fun(N, R, N-R)
    # else:
    #     fun(N, N-R, R)

    print(f"#{test_case}",1)