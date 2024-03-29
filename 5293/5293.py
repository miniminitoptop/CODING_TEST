# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for test_case in range(1,T+1):
#     A, B, C, D = map(int,input().split())
#     total = A+B+C+D + 1
#     lst = []
#     ans = " "
#     rec = " "
#
#     if A == 0 and B ==0 and C == 0 and D == 0:
#         print(f'#{test_case} impossible')
#         continue
#
#     while not ( A == 0 and B ==0 and C == 0 and D == 0):
#
#         err_chk1 = 0
#         err_chk2 = 0
#
#         if D != 0:
#             D -= 1
#             rec = '11'
#             if C != 0 :
#                 C -= 1
#                 rec = '110'
#                 if B != 0 :
#                     B -= 1
#                     rec = '0110'
#                     if A != 0:
#                         A -= 1
#                         rec = '01100'
#                 else:
#                     if A != 0:
#                         A -= 1
#                         rec = '1100'
#             else:
#                 if B != 0 :
#                     B -= 1
#                     rec = '011'
#                     if A != 0:
#                         A -= 1
#                         rec = '0011'
#                 else:
#                     if A != 0:
#                         A -= 1
#                         if len(lst) >= 1:
#                             for i in range(len(lst)):
#                                 for j in range(len(lst[i])):
#
#                                     if (lst[i][j] == '1' and lst[i][j+1] == '1') and err_chk1 == 0:
#                                         lst[i] = lst[i][0:j+1] + '1' + lst[i][j+1:]
#                                         rec = "good"
#                                         err_chk1 = 1
#
#                                     if ((lst[i][j] == '0' and lst[i][j+1] == '0') or (lst[i][j] == '0' and lst[i][j+1] == '1') or (lst[i][j] == '1' and lst[i][j+1] == '0')) and err_chk2 == 0:
#                                         lst[i] = lst[i][0:j + 1] + '0' + lst[i][j + 1:]
#                                         rec = "good"
#                                         err_chk2 = 1
#
#                                 if err_chk1 != 1 or err_chk2 != 1:
#                                     rec = "impossible"
#                                     lst.append(rec)
#                                     break
#                         else:
#                             rec = "impossible"
#                             lst.append(rec)
#                             break
#
#
#         else:
#             if C != 0:
#                 C -= 1
#                 rec = '10'
#                 if B != 0:
#                     B -= 1
#                     rec = '010'
#                     if A != 0:
#                         A -= 1
#                         rec = '0010'
#                 else:
#                     if A != 0:
#                         A -= 1
#                         rec = '100'
#             else:
#                 if B != 0 :
#                     B -= 1
#                     rec = '01'
#                     if A != 0:
#                         A -= 1
#                         rec = '001'
#                 else:
#                     if A != 0:
#                         A -= 1
#                         rec = '00'
#         lst.append(rec)
#
#     ans = lst[0]
#
#     if "impossible" in lst:
#         ans = "impossible"
#
#     if len(lst)>1:
#         for i in range(1, len(lst)):
#
#             if ans[0] == lst[i][len(lst[i])-1] :
#                 ans = lst[i][0:len(lst[i])] + ans[1:]
#                 continue
#
#             if ans[len(ans)-1] == lst[i][0]:
#                 ans = ans[0:len(ans)] + lst[i][1:]
#                 continue
#
#             else:
#                 ans = "impossible"
#                 break
#
#     print(f'#{test_case} {ans}')
#
#
#
#
#
#
T = int(input()) + 1
ans = []

for t in range(1, T):
    a, b, c, d = map(int, input().split())

    if a and not b and not c and not d:
        result = "0" * (a + 1)

    elif d and not a and not b and not c:
        result = "1" * (d + 1)

    elif b == c and b:
        result = "0" * (a + 1) + "10" * (b - 1) + "1" * (d + 1) + "0"

    elif b - c == 1:
        result = "0" * (a + 1) + "10" * c + "1" * (d + 1)

    elif c - b == 1:
        result = "1" * (d + 1) + "01" * b + "0" * (a + 1)

    else:
        result = "impossible"
    ans.append(result)

ans2 = "\n".join(ans)

print(ans2)