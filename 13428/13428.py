import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N = list(map(int, input()))
    M = list(map(int, N[::-1]))

    max_idx = len(M)-1-M.index(max(M[0:]))
    min_idx = len(M)-1-M.index(min(M[0:]))

    for i in range(len(N)):
        print(max_idx, min_idx)

        if i == min_idx:
            min_idx = len(M)-1-M.index(min(M[0:(len(M)-i)]))
            print(min_idx)

    # min_num = "".join(list(map(str, N)))
    # max_num = "".join(list(map(str, N)))
    # print(min_num, max_num)


