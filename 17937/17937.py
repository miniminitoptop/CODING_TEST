import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    lst1 = []
    for i in range(1,lst[0]+1):
        if lst[0] % i == 0 and lst[1] % 1 == 0:
            lst1.append(i)
        
    print(lst1)
    #최대 공약수의 범위는 1부터 A(lst[0])까지
    
    