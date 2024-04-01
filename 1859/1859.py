import sys
sys.stdin = open("input.txt","r")

T = int(input())
lst2 = []

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst = lst[::-1]
    bst_price = lst[0]
    bst_b = 0

    for i in lst:
        if i < bst_price:
            bst_b += bst_price - i
        else:
            bst_price = i

    lst2.append(f"#{test_case} {bst_b}")

for i in lst2:
    print(i)
