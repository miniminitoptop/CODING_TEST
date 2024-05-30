import sys
sys.stdin = open("input.txt", "r")

ans = []

for test_case in range(1,11):
    T = int(input())
    lst = list(input() for _ in range(100))
    lst1 = list("".join([lst[j][i] for j in range(100)]) for i in range(100))

    ans = 0

    for i in range(100):
        br = 0
        for j in range(100):
            for k in range(100):
                if lst1[k][j:j+i] == lst1[k][j:j+i][::-1]:
                    ans = max(len(lst1[k][j:j+i]), ans)
                    br = 1
                    break
                elif lst[k][j:j+i] == lst[k][j:j+i][::-1]:
                    ans = max(len(lst[k][j:j + i]), ans)
                    br = 1
                    break
            if br == 1:
                break

    print(f"#{test_case}", ans)


