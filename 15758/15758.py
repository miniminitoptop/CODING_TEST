import sys
sys.stdin = open("input.txt","r")


for test_case in range(1,int(input())+1):
    S, T = input().split()
    ans = "no"

    if S * len(T) == T * len(S):
        ans = "yes"

    print(f"#{test_case} {ans}")
