import sys
sys.stdin = open("input.txt", "r")

import math

T = int(input())
lst = []

for test_case in range(1, T+1):
    N = int(input())
    ans = 0

    for i in range(N):
        x, y = map(int, input().split())
        r = math.ceil((((x ** 2) + (y ** 2))**(1/2))/20)

        if r == 0:
            ans += 10
        elif r <= 11:
            ans += (11 - r)


        # if ra >= 0 and ra <= (20 ** 2):
        #     ans += 10
        # elif ra > (20 ** 2) and ra <= (40 ** 2):
        #     ans += 9
        # elif ra > (40 ** 2) and ra <= (60 ** 2):
        #     ans += 8
        # elif ra > (60 ** 2) and ra <= (80 ** 2):
        #     ans += 7
        # elif ra > (80 ** 2) and ra <= (100 ** 2):
        #     ans += 6
        # elif ra > (100 ** 2) and ra <= (120 ** 2):
        #     ans += 5
        # elif ra > (120 ** 2) and ra <= (140 ** 2):
        #     ans += 4
        # elif ra > (140 ** 2) and ra <= (160 ** 2):
        #     ans += 3
        # elif ra > (160 ** 2) and ra <= (180 ** 2):
        #     ans += 2
        # elif ra > (180 ** 2) and ra <= (200 ** 2):
        #     ans += 1

    lst.append(f'#{test_case} {ans}')

for i in lst:
    print(i)

