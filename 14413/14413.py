import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, int(input()) + 1):
    N,M = map(int,input().split())
    blk = 0
    wht = 0
    blk_pos = 0
    wht_pos = 0
    impos = 0
    
    lst = []
    
    for i in range (N):
        lst.append(input())

        if '#' in lst[i]:
            blk_pos = (i + lst[i].index('#'))%2
            blk +=1  
            
        if '.' in lst[i]:
            wht_pos = (i + lst[i].index('.'))%2
            wht += 1
            
       
    if wht != 0 and blk !=0 and blk_pos == wht_pos:
        impos = 1
           
    for i in range(N):
        for j in range(M):
            if lst[i][j] == '#' and (i+j)%2 != blk_pos:
                    impos = 1
                    break
                       
            elif lst[i][j] == '.' and  (i+j) %2 != wht_pos:
                    impos = 1
                    break
                    
    if impos == 1:
        print(f'#{test_case} impossible')
        continue
    
    print(f'#{test_case} possible')
    
    
    
    
            
             
            