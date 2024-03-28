import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for test_case in range(1, T+1):
    K = int(input())
    y = K
    i = 1
    poi_count = 0 
    
    while i < K: 
        if (i*i)+(y*y) <= K*K:
            poi_count += y     
        else:
            i = i - 1
            y = y - 1
        i = i + 1
            
    print(f"#{test_case} %d" %(1+(K*4)+(poi_count*4)))
    
    

    
    