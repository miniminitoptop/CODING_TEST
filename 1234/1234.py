import sys
sys.stdin = open("input.txt", "r")

for T in range(1, 11):
    N, M = map(str, input().split())
    lst = list(map(str, M))

    i = 0
    while True:

        if i == len(lst)-1:
            break

        if lst[i] == lst[i+1]:
            lst = lst[:i]+lst[i+2:]
            i = 0
            continue

        i += 1

    print(f"#{T}","".join(lst))







