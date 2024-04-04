import sys
import datetime

sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(t):

    c = input()
    try:
        d = datetime.datetime.strptime(c, '%Y%m%d')
        print(f'#{i + 1} %s' % d.strftime('%Y/%m/%d').zfill(10))

    except:
        print(f'#{i + 1} -1')

# T = int(input())
#
# for test_case in range(1, T+1):
#     N = input()
#     year = int(N[0:4])
#     month = int(N[4:6])
#     day = int(N[6:])
#
#     ans = N[0:4] + "/" + N[4:6] + "/" + N[6:]
#
#     day_lst = list(i for i in range(1, 32))
#
#     if month == 2:
#         day_lst.pop()
#         day_lst.pop()
#         day_lst.pop()
#
#     elif month in [4, 6, 9, 11]:
#         day_lst.pop()
#
#     if month < 1 or month > 12:
#         ans = "-1"
#
#     if day not in day_lst:
#         ans = "-1"
#
#     print(f"#{test_case} {ans}")