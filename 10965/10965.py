import sys
sys.stdin = open("input.txt", "r")

prime = [2]

for i in range(3, int(10000000**0.5),2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)

# / = 'float' , // = 'int'
     
T = int(input())
ans = []

for test_case in range(1, T + 1):
   K = int(input())
   res = 1
   
   if K**0.5 != int(K**0.5):
        for p in prime:
           cnt = 0
           while not K % p:
               K //= p
               cnt += 1
               if cnt % 2:
                    res *=p
               elif not cnt % 2:
                    res //=p 
               if K == 1 or p > K:
                   break
        if K > 1:
             res *= K
                
         
   ans.append(f'#{test_case} {res}')
       
   
    

for i in range (len(ans)):
    
    print(ans[i])
    

   
 
          