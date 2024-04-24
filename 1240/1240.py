import sys
sys.stdin = open("input.txt","r")

for test_case in range(1,int(input())+1):
    N,M = map(int,input().split())

    lst = list(input() for _ in range(N))
    lst2 = ""

    for i in lst:
        if '1' in i:
            lst2 = i
            break

    lst2 = lst2[::-1]
    idx = lst2.index("1")
    lst2 = lst2[idx:idx+56]
    lst2 = lst2[::-1]

    shin = 0
    sang = 0

    for i in range(0,50,7):
        mnt = 0
        if lst2[i:i+7] == "0001101":
            mnt = 0
        elif lst2[i:i + 7] == "0011001":
            mnt = 1
        elif lst2[i:i + 7] == "0010011":
            mnt = 2
        elif lst2[i:i + 7] == "0111101":
            mnt = 3
        elif lst2[i:i + 7] == "0100011":
            mnt = 4
        elif lst2[i:i + 7] == "0110001":
            mnt = 5
        elif lst2[i:i + 7] == "0101111":
            mnt = 6
        elif lst2[i:i + 7] == "0111011":
            mnt = 7
        elif lst2[i:i + 7] == "0110111":
            mnt = 8
        elif lst2[i:i + 7] == "0001011":
            mnt = 9

        if (i+1)%2 == 0:
            shin += mnt
        else:
            sang += mnt

    ans = shin + sang

    if (sang * 3 + shin)%10 != 0:
        ans = 0

    print(f"#{test_case}", ans)









