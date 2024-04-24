import sys
sys.stdin = open("input.txt","r")

for i in range(10):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    arr_sum = 0
    cro_sum = 0
    col_sum = [0]*100

    for j in range(100):
        arr_sum = max(sum(lst[j]), arr_sum)
        cro_sum += lst[j][j]

        for k in range(100):
            col_sum[k] += lst[j][k]

    print(f"#{i+1}",max(max(col_sum),cro_sum,arr_sum))


