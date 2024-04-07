import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    S = input()
    ans = "YES"
    if S.count("x") > 7:
        ans = "NO"
    print(f"#{test_case} {ans}")