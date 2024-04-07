import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    num = 0
    arr = list()
    n = 0
    for i in range(7):
        n += 1
        if lst[i] == 1:
            num += 1
            arr.append(n)
            n = 0
    arr[0] += n
    print(arr)

    q, r = divmod(N, num)

    res = q * 7

    if r == 0:
        res -= max(arr) - 1

    else:
        arr *= 2
        s = 8
        for i in range(num):
            print(arr[i:i + r - 1])
            s = min(s, sum(arr[i:i + r - 1]))
        res += s + 1

    print(f"#{test_case} {res}")

    # rest = N % lst.count(1)
    #
    # max_val = int("".join(list(map(str, lst))))
    #
    # for i in range(7):
    #     mnt = lst.pop()
    #     lst.insert(0, mnt)
    #     max_val = max(max_val, int("".join(list(map(str, lst)))))
    #
    # lst = list(map(int, list(str(max_val))))
    #
    # cnt = 0
    #
    # if rest == 0:
    #     ans = (N // (1 + lst.count(1)))*7
    #     for i in range(7):
    #         if lst[i] == 1:
    #             cnt += 1
    #             if cnt == lst.count(1):
    #                 ans += i+1
    # else:
    #     ans = (N // (lst.count(1)))*7
    #     for i in range(7):
    #         if lst[i] == 1:
    #             cnt += 1
    #             if cnt == rest:
    #                 ans += i+1
    #
    # print(f"#{test_case} {ans}")

