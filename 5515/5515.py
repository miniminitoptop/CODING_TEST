import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    m, d = map(int,input().split())

    lst = [4,0,1,4,6,2,4,0,3,5,1,3]

    print(f"#{test_case}",(lst[m-1]+d-1)%7)