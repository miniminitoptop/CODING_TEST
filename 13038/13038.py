import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    rest = N % lst.count(1)

    max_val = int("".join(list(map(str, lst))))

    for i in range(7):
        mnt = lst.pop()
        lst.insert(0,mnt)
        max_val = max(max_val,int("".join(list(map(str, lst)))))

    lst =




    # cnt = 0
    #
    # if rest == 0:
    #     ans = (N // (1 + lst.count(1)))*7 - lst.index(1)
    #     for i in range(7):
    #         if lst[i] == 1:
    #             cnt += 1
    #             if cnt == lst.count(1):
    #                 ans += i+1
    # else:
    #     ans = (N // (lst.count(1)))*7 - lst.index(1)
    #     for i in range(7):
    #         if lst[i] == 1:
    #             cnt += 1
    #             if cnt == rest:
    #                 ans += i+1
    #
    # print(f"#{test_case} {ans}")

