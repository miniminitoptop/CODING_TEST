import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input())+1):
    lst = list(map(int,input()))

    i = 0
    ans = 0

    while True:

        if 1 not in lst:
            break

        if lst[i] == 1:
            ans += 1
            for j in range(i, len(lst)):
                lst[j] = lst[j] ^ 1

        i += 1

    print(f"#{test_case}", ans)


