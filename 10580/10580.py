import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    lst2 = []
    cnt = 0

    for i in range(N):
        lst1 = list(map(int,input().split()))
        lst2.append(lst1)

    for i in lst2:
        for j in lst2:
            if (j[0] < i[0] and j[1] > i[1]) or (j[0] > i[0] and j[1] < i[1]):
                cnt += 1

    print(f"#{test_case} {cnt//2}")
