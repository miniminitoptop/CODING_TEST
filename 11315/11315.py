import sys
sys.stdin = open("input.txt","r")

def chk_omok(x, y):
    A = B = crs_up = crs_down = 1
    ans = "no"
    for i in range(1, 5):
        if 0 <= y+i < N and lst[x][y+i] == "o":
            A += 1
        if 0 <= x+i < N and lst[x+i][y] == "o":
            B += 1
        if 0 <= x+i < N and 0 <= y+i < N and lst[x+i][y+i] == "o":
            crs_up += 1
        if 0 <= x-i < N and 0 <= y+i < N and lst[x-i][y+i] == "o":
            crs_down += 1
        if A == 5 or B == 5 or crs_up == 5 or crs_down == 5:
            ans = "Yes"
            break
    return ans

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    out = 0
    ans = "No"

    for i in range(N):
        for j in range(N):
            if lst[i][j] == "o":
                ans = chk_omok(i,j)
            if ans == "Yes":
                out = 1
                break
        if out == 1:
            break

    print(f"#{test_case} {ans}")



