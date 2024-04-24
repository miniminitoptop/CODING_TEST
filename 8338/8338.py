import sys
sys.stdin = open("input.txt", "r")

for i in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0

    for j in lst:
        ans = max(ans+j, ans*j)

    print(f"#{i+1}", ans)
