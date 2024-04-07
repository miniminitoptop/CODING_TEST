import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    n,m = map(int, input().split())
    lst = []
    ans = "yes"

    for i in range(n):
        lst.append(input())

    lst_a = list(lst[0])
    lst_b = list(lst[i][0] for i in range(n))

    for i in range(n):

        for j in range(m):
            if lst_a[j] == lst_b[i] and lst[i][j] != "0":
                ans = "no"
                break
            elif lst_a[j] != lst_b[i] and lst[i][j] != "1":
                ans = "no"
                break
        if ans == "no":
            break

    print(f"#{test_case} {ans}")