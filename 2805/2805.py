import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    lst = [list(map(int,input())) for _ in range(N)]

    ans, cnt = 0, 0

    left_idx, right_idx = N//2, N//2+1

    while True:
        ans += sum(lst[cnt][left_idx:right_idx])

        print(lst[cnt][left_idx:right_idx])
        cnt += 1

        if cnt > N//2:
            left_idx += 1
            right_idx -= 1
        else:
            left_idx -= 1
            right_idx += 1

        if cnt == N:
            break

    print(f"#{test_case}",ans)






