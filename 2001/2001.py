import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input())+1):

    N, M = map(int, input().split())
    lst = []
    lst1 = [0]*(N-M+1)

    cnt = 0
    ans = 0

    for j in range(N):
        lst.append(list(map(int, input().split())))
        cnt += 1

        for k in range(N-M+1):
            lst1[k] += sum(lst[j][k:M+k])
            ans = max(ans, max(lst1))

            if cnt == M:
                lst1[k] -= sum(lst[j-M+1][k:M+k])

        if cnt == M:
            cnt -= 1

    print(f"#{test_case} {ans}")





