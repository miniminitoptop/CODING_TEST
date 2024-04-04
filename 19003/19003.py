import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    A, B = map(int, input().split())
    lst = []

    for i in range(0,A):
        lst.append(input())

    print(lst)











