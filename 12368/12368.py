import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    ans = 0
    idx = 0
    idx2 = N-1

    for i in range(N):
        lst.append(input())

    a = "".join(lst)
    b = a[::-1]
    print(a)
    print(len(a))
    print(b)
    print(len(b))

    #
    # for i in range(N-1, -1, -1):
    #
    #     for j in range(idx, i):
    #
    #         if lst[j] == lst[i][::-1]:
    #             idx = j
    #             idx2 = i
    #             ans += 2*M
    #             break
    # if idx2 - idx > 1:
    #     for i in range(idx+1, idx2):
    #
    #         if lst[i] == lst[i][::-1]:
    #             ans += M
    #             break

    print(f"#{test_case} {ans}")








