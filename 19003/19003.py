import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split())
    lst = []

    for i in range(N):
        lst.append(input())

    for i in range(N):
        if lst[i] in lst[N-1-i::-1]:










    # for i in range(N):







