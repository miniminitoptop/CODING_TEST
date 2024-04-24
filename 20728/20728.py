import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    lst = sorted(list(map(int, input().split())),reverse=True)
    ans = 99999999999

    for i in range(0,N-1):
        if len(lst[i:i+K]) != K:
            break
        ans = min(ans,max(lst[i:i+K])-min(lst[i:i+K]))

    print(f"#{test_case}",ans)