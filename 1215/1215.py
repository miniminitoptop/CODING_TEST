import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    lst = [input() for _ in range(8)]
    lst += [[lst[j][i] for j in range(8)] for i in range(8)]
    ans = 0
    print(lst)

    for l in range(16):
        for k in range(9-N):
            if lst[l][k:k+N] == lst[l][k:k+N][::-1]:
                ans += 1

    print(f"#{test_case}", ans)




