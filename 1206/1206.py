import sys
sys.stdin = open("sample_input.txt","r")


for test_case in range(1, 11):
    T = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    
    for i in range(2,T-2):
        mx = lst[i-2]
        for j in range(i-1, i+3):
            if j == i:
                continue
            else:
                if mx < lst[j]:
                    mx = lst[j]
    
        if lst[i]>mx:
            ans += (lst[i]-mx)
            

    print(f'#{test_case} {ans}')