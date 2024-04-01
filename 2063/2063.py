import sys
sys.stdin = open("input.txt","r")

N = int(input())

lst = list(map(int,input().split()))
lst.sort()

print(lst[int(N/2)])


# for i in range