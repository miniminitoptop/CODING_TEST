import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    M,N = map(str, input().split())
    N = int(N)
    lst2 = list(map(int,str(M)))
    lst2.reverse()
   
    tm = 0
    shin = 0
    
    lst_len = len(lst2)
    
    if N != 0 :
        for i in range(lst_len-1,-1,-1):
                max_num = max(lst2[0:i+1])
                max_idx = lst2.index(max_num)
                
                if lst2[i] < lst2[max_idx]:
                    mnt = lst2[i]
                    lst2[i] = lst2[max_idx]
                    lst2[max_idx] = mnt
                    tm +=1
                    if tm == N:
                        break
                               
        if tm<N and (N-tm)%2 != 0:  
            for i in lst2 :
                if lst2.count(i) > 1:
                    shin = 1
                    break
            if shin == 0:
                mnt = lst2[1]
                lst2[1] = lst2[0]
                lst2[0] = mnt
    
    lst2.reverse()
    sang = ''.join(str(i) for i in lst2)
    print(f'#{test_case} {sang}')
    
    