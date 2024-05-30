import sys
sys.stdin = open("input.txt", "r")

def dfs(ls, st1, st2, visit):

    global ans

    v1 = [0, 0, 1, -1]
    v2 = [1, -1, 0, 0]

    for i in range(4):

        if ls[st1 + v1[i]][st2 + v2[i]] == 3:
            ans = 1
            return

        elif ls[st1 + v1[i]][st2+v2[i]] == 0 and (st1 + v1[i], st2 + v2[i]) not in visit:
            visit.append((st1 + v1[i], st2 + v2[i]))
            dfs(ls, st1 + v1[i], st2 + v2[i], visit)

for test_case in range(1, 11):

    T = int(input())

    lst = [list(map(int, input())) for _ in range(16)]

    v = [(1, 1)]

    ans = 0

    dfs(lst, 1, 1, v)

    print(v)
    print(f"#{T}", ans)









