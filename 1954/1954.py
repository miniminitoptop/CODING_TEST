import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):

    N = int(input())

    lst = [[0]*N for _ in range(N)]

    v1 = [0, 1, 0, -1]
    v2 = [1, 0, -1, 0]

    idx1, idx2, i = 0, 0, 0

    for num in range(1, N*N+1):
        lst[idx1][idx2] = num

        x = idx1 + v1[i]
        y = idx2 + v2[i]

        if 0 <= x < N and 0 <= y < N and lst[x][y] == 0:
            idx1, idx2 = x, y

        else:
            i = (i + 1) % 4
            idx1 += v1[i]
            idx2 += v2[i]

    print(f"#{test_case}")

    for i in lst:
        print(" ".join(list(map(str,i))))







