import sys
sys.stdin = open("input.txt", "r")

def rook():
    lst = []
    lst2 = [0]*8
    
    for i in range(0,8):
        lst.append(input())
        
    for j in range(0,8):
        if lst[j].count('O') != 1 :
            return False
        
        lst2[lst[j].index('O')] = 1
    
    
    if lst2.count(1) == 8:
        return True       
    else:
        return False

T = int(input())
for test_case in range(1, T + 1): 
    
    if rook():
        print(f'#{test_case} yes')  
    else:
        print(f'#{test_case} no')
    
    

    