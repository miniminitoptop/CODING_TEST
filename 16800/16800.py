import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = []
    ans = 0
    x,y = 1,1 
    i = 2
        
    if (N) ** (1/2) == int((N) ** (1/2)):
        ans = int((N) ** (1/2))*2 - 2
    
    
    else:
        while i < int(N**(1/2))+1:
            if N % i == 0:
                N //= i
                x *= i
                
                tmp = x
                x = y
                y = tmp
            
            else:
                i +=1
        if x < y:
            x *= N
        else:
            y *= N
        
        print(x,y)

        # if len(lst) > 3:
        #     for i in range(0,c):

        #         b *= lst.pop() * lst.pop(lst.index(min(lst)))
        #         d *= lst.pop() * lst.pop(lst.index(min(lst)))

        #         tmp = b
        #         b = d
        #         d = b
        #     ans = b + d - 2
        
        # elif len(lst) == 3:
        #     ans = lst[0]*lst[2] + lst[1] -2

        # elif len(lst) == 2:
        #     ans = lst[0] + lst[1] - 2
            
        # elif len(lst) == 1:
        #     ans = lst[0] - 1
                
        # print(f'#{test_case} {ans}')
        
                
        