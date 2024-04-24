import sys
sys.stdin = open("sample_input.txt", "r")

for test_case in range(1, 11):
    T = int(input())
    lst = list(map(int, input().split()))

    ans = 0

    for i in range(2, len(lst)-2):

        if lst[i] > max(max(lst[i-2:i]), max(lst[i+1:i+3])):
            ans += lst[i] - max(max(lst[i-2:i]), max(lst[i+1:i+3]))

    print(f"{test_case}",ans)