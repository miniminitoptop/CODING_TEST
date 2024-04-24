import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range (1, T+1):
    N = int(input())

    in_str = input().replace('!', '.').replace('?','.')
    lst1 = list(in_str.split("."))

    lst = [i for i in lst1 if i != ""]

    print(lst)

    ans_lst = [0 for i in range(N)]

    for i in range(len(lst)):
        lst[i] = lst[i].split()

        for j in range(len(lst[i])):
            if "A" <= lst[i][j][0] <= "Z":
                no = 0
                for k in range(1, len(lst[i][j])):
                    if not "a" <= lst[i][j][k] <= "z":
                        no = 1
                        break
                if no == 1:
                    continue
                ans_lst[i] += 1

    print(f'#{test_case} {" ".join(list(map(str,ans_lst)))}')

