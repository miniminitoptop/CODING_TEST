import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    lst = [list(input().split()) for _ in range(100)]

    ans = 0

    for i in range(N):
        mnt = ""
        for j in range(N):
            if lst[j][i] == "1" or lst[j][i] == "2":
                mnt += lst[j][i]
        ans += mnt.count("12")

    print(f"#{test_case}", ans)
