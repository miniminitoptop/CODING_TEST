import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range (1,T+1):
    N, M = map(int,input().split())
    lst1 = [0 for _ in range(N)]
    lst2 = [0 for _ in range(M)]
    lst3 = [0 for _ in range(2*M)]

    for i in range(N):
        lst1[i] = int(input())
    print("lst1 : ", lst1)
    for i in range(M):
        lst2[i] = int(input())
    print("lst1 : ", lst2)
    for i in range(2*M):
        lst3[i] = int(input())
    print("lst1 : ", lst3)

    print("-----------------------------")