import sys
sys.stdin = open("sample.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    
    lst = f'#{test_case} '
    for j in range(K):
        lst += (f"1/{K} ")
        
    print(lst)