T = int(input())

lst = []

for test_case in range(1,T+1):
    N, PD, PG = map(int,input().split())
    K = 1
    for i in range (1,101):
        if PD % i == 0 and 100 % i == 0:
            K = max(K, i)

    C = 100//K

    if C > N:
        lst.append(f'#{test_case} Broken')
    else:
        if (PG == 100 and PD != 100) or (PG == 0 and PD != 0):
            lst.append(f'#{test_case} Broken')
        else:
            lst.append(f'#{test_case} Possible')

for i in lst:
    print(i)

# 철자를 잘보자