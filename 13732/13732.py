import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    lst = []
    min_x, max_x, min_y, max_y = 21, 0, 21, 0
    no = 0

    for y in range(N):
        lst.append(list(input()))
        for x in range(N):
            if lst[y][x] == '#':
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    if max_x - min_x != max_y - min_y:
        print(f'#{test_case} no')
        continue

    for i in lst[min_y:max_y+1]:
        for j in i[min_x:max_x+1]:
            if j == '.':
                no = 1
                break
        if no == 1:
            break

    if no == 1:
        print(f'#{test_case} no')
        continue

    print(f'#{test_case} yes')




