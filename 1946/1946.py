import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    lst = []

    for i in range(N):
        A, B = input().split()
        lst += A*int(B)

    # arr = "".join(lst)
    #
    # start_idx = 0
    #
    print(f'#{test_case}')
    print(len(lst))

    for i in range (0,len(lst),10):
        print("".join(lst[i:i+10]))

    #문자열 뒤는 범위를 초과해도 상관이 없다.
    # print(arr[start_idx:])

