import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst = lst[::-1]
    bst_price = lst[0]
    bst_b = 0
    i = 0

    while i < N:
        if lst[i] < bst_price:
            bst_b += bst_price - lst[i]
        else:
            bst_price = lst[i]

        i += 1

    print(f"#{test_case} {bst_b}")

