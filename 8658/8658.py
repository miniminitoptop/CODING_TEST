import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    lst = list(map(int,input().split()))
    ans1 = 0
    ans2 = 54

    for i in lst:
        len_num = len(str(i))
        sum = 0
        num = i

        for j in range(len_num-1, -1, -1):
            sum += num//(10**j)
            num %= (10**j)

        ans1 = max(ans1, sum)
        ans2 = min(ans2, sum)

    print(f"#{test_case} {ans1} {ans2}")