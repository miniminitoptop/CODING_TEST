import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, int(input())+1):
    N = int(input())
    lst = sorted(list(map(int, input().split())))

    ans = -1
    br = 0

    for i in range(N-2, -1, -1):
        for j in range(N-1, i, -1):
            if sorted(list(map(int, str(lst[i]*lst[j])))) == list(map(int, str(lst[i]*lst[j]))):
                ans = lst[i]*lst[j]
                br = 1
                break
        if br == 1:
            break

    print(f"#{test_case} {ans}")






