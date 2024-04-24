import sys
sys.stdin = open("input.txt","r")

for i in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    for j in range(N):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1

    print(f"#{i}", max(lst)-min(lst))
