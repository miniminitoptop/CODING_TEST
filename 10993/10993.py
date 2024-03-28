import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input())+1):
    N = int(input())
    S = 0
    lst1 = []
    lst2 = ['0']*N
    lst2[0] = 'K'
    for i in range(N):
        lst1.append(list(map(int,input().split())))

        if lst1[i][2] > S :
            S = lst1[i][2]
            lst2 = ['0']*N
            lst2[i] = 'K'
        elif lst1[i][2] == S :
            lst2[i] ='k'

    print(lst2)



