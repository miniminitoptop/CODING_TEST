import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    lst = list(map(str, input().split()))

    lst_zero = ['C','E','F','G','H','I','J','K','L','M','N','S','T','U','V','W','X','Y','Z']
    lst_one = ['A','D','O','P','Q','R']
    arr = [" "," "]
    ans = "SAME"

    for i in range(2):
        for j in range(len(lst[i])):
            if lst[i][j] in lst_zero:
                arr[i] += "o"
            elif lst[i][j] in lst_one:
                arr[i] += "i"
            else:
                arr[i] += "B"

    if arr[0] != arr[1]:
        ans = "DIFF"

    print(f"#{test_case} {ans}")
