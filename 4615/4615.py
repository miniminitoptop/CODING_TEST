import sys
sys.stdin = open("input.txt", "r")
def change_lst(j, Y, X, D):

    global lst
    global ls1

    ls1[Y][X] = D

    Y += v1[j]
    X += v2[j]

    if (Y < 0 or N - 1 < Y) or (X < 0 or N - 1 < X):
        ls1 = [i[:] for i in lst]
        return

    if ls1[Y][X] != D and ls1[Y][X] != 0:
        change_lst(j, Y, X, D)

    if ls1[Y][X] == 0:
        ls1 = [i[:] for i in lst]
        return

    if ls1[Y][X] == D:
        lst = [i[:] for i in ls1]
        return

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    ran = N//2-1
    v1 = [1, -1, 0, 0, 1, 1, -1, -1]
    v2 = [0, 0, 1, -1, -1, 1, -1, 1]
    lst = [[0] * N for i in range(ran)]
    lst += [[0] * ran + [2, 1] + [0] * ran]
    lst += [[0] * ran + [1, 2] + [0] * ran]
    lst += [[0] * N for i in range(ran)]

    ans1 = 0
    ans2 = 0

    for j in range(M):
        Y, X, D = map(int, input().split())

        lst[Y-1][X-1] = D
        ls1 = [i[:] for i in lst]

        for i in range(8):
            if not (0 <= Y-1+v1[i] < N and 0 <= X-1+v2[i] < N):
                continue

            if ls1[Y-1 + v1[i]][X-1 + v2[i]] != D and ls1[Y-1 + v1[i]][X-1 + v2[i]] != 0:
                change_lst(i, Y-1 + v1[i], X-1 + v2[i], D)

    for i in lst:
        ans1 += i.count(1)
        ans2 += i.count(2)

    print(f"#{test_case}", ans1, ans2)


