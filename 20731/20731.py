import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    for i in range(N):
        print(lst[i][i:])