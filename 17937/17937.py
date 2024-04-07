import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))

    if lst[0] == lst[1]:
        ans = lst[0]
    else:
        ans = 1

    print(f"#{test_case} {ans}")
    #최대 공약수의 범위는 1부터 A(lst[0])까지
    
    