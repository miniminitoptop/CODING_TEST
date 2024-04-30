import sys
sys.stdin = open("input.txt","r")

def dfs(n, l2, pt1, pt2):
    global win_cnt
    global lose_cnt

    if n == 9 and pt1 > pt2:
        win_cnt += 1

    elif n == 9 and pt1 < pt2:
        lose_cnt += 1
    mnt1, mnt2 = pt1, pt2

    for i in range(len(l2)):

        if lst[n] > l2[i]:
            pt1 += (n+l2[i])
        elif lst[n] < l2[i]:
            pt2 += (n+l2[i])

        lst3 = [s for s in l2 if s != l2[i]]
        dfs(n+1, lst3, pt1, pt2)

        pt1, pt2 = mnt1, mnt2


T = int(input())

for test_case in range(1,T+1):
    lst = list(map(int,input().split()))
    lst2 = [i for i in range(1, 19) if i not in lst]

    win_cnt = 0
    lose_cnt = 0

    dfs(0, lst2, 0, 0)

    print(win_cnt, lose_cnt)








