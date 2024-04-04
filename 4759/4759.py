import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range (1, T+1):
    in_str = input()
    ans = "Exist"
    min_st_idx = 21
    max_st_idx = 0

    if "*" in in_str:
        for i in range(len(in_str)):
            if in_str[i] == "*":
                min_st_idx = min(min_st_idx, i)
                max_st_idx = max(max_st_idx, i)

        if len(in_str) - 1 - max_st_idx <= min_st_idx:
            if in_str[max_st_idx+1:][::-1] != in_str[0:len(in_str) - 1 - max_st_idx]:
                ans = "Not exist"
        else:
            if in_str[0:min_st_idx][::-1] != in_str[len(in_str) - min_st_idx:]:
                ans = "Not exist"
    else:
        for i in range(0, len(in_str)//2):
            if in_str[i] != in_str[len(in_str)-1-i]:
                    ans = "Not exist"
                    break

    print(f"#{test_case} {ans}")

# T = int(input())
#
# for t in range(1, T + 1):
#     word = input()
#     words = word.split('*')
#     first, last = words[0], words[-1]
#
#     if first in last[::-1] or last in first[::-1]:
#         print(f'#{t} Exist')
#     else:
#         print(f'#{t} Not exist')