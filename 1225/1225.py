import sys
sys.stdin = open("input.txt","r")

for test_case in range(1,11):
    n = int(input())
    lst = list(map(int,input().split()))
    cnt = 0

    while True:

        lst.append(lst.pop(0)-(cnt%5)-1)
        cnt += 1

        if lst[7] <= 0:
            lst[7] = 0
            break

    print(f'#{test_case}', *lst)
