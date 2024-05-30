def dfs(X, Y, N, cnt):

    global answer

    if X > Y:
        return

    if X == Y:
        answer = min(answer, cnt)
        print(answer)

    dfs(X * 2, Y, N, cnt + 1)
    dfs(X * 3, Y, N, cnt + 1)
    dfs(X + N, Y, N, cnt + 1)


def solution(x, y, n):
    if x == y:
        return 0

    answer = 9999999999999999999999999999999999999999999999

    dfs(x, y, n, 0)

    if answer == 0:
        answer = -1

    print(answer)
    return answer

solution(10,40,5)