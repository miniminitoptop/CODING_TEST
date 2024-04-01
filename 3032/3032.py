import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    A, B = map(int,input().split())
    lst = []

    if A > B:
        X1, Y1 = 1, 0
        X2, Y2 = 0, 1
    else:
        X1, Y1 = 0, 1
        X2, Y2 = 1, 0

    R1 = max(A, B)
    R2 = min(A, B)
    Q = 0

    while R2 > 0:
        Q = R1 // R2
        mnt1, mnt2 = X1, Y1
        X1, Y1 = X2, Y2
        X2, Y2 = (mnt1 - (Q * X2)), (mnt2 - (Q * Y2))
        mnt3 = R1
        R1 = R2
        R2 = mnt3 % R2

        if R2 == 1:
            print(f"#{test_case} {X2} {Y2}")
            break

    else:
        print(f'#{test_case} -1')





















