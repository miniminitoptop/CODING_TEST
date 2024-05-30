import sys
sys.stdin = open("input.txt", "r")

def fds(ls,n):

    global ans

    if 99 in ls[n]:
        ans = 1
        return

    for i in ls[n]:
        fds(ls, i)

for test_case in range(1, 11):
    T, N = map(int, input().split())
    lst = list(map(int, input().split()))

    lst1 = [[]for _ in range(100)]

    for i in range(0, 2*N, 2):
        lst1[lst[i]].append(lst[i+1])

    ans = 0

    fds(lst1,0)

    print(f"#{test_case}", ans)
