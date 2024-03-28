import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    
    N, M = map(int,input().split())
    lst1 = list(map(str,input().split()))
    lst2 = list(map(str,input().split()))
                
    Q = int(input())
    
    ans = f'#{test_case} '
    for i in range(Q):
        Y = int(input()) - 1
        lst1_idx, lst2_idx = Y%N, Y%M
        ans += f'{lst1[lst1_idx]}'+f'{lst2[lst2_idx]}'+' '
    
    print(ans)
        
   
    
    
    
 