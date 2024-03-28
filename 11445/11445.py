import sys
sys.stdin = open("input.txt", "r")

T = int(input())
answer = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Q = input().split()[0], input().split()[0]

    if P + 'a' == Q:  # man vs mana
        answer.append(f"#{test_case} N")

    else:
        answer.append(f"#{test_case} Y")

print('\n'.join(answer))

# T = int(input())
#
# for test_case in range(1, T + 1):
#     P, Q = input().split()[0], input().split()[0]
#
#     if P == Q:
#         print(f'#{test_case} N')
#         continue
#
#     sht_len = min(len(P),len(Q))
#
#     for i in range(sht_len):
#         if P[i] != Q[i]:
#             print(f'#{test_case} Y')
#             break
#
#
#     else:
#         if Q[sht_len] == 'a':
#             if len(Q) > sht_len +1:
#                 print(f'#{test_case} Y')
#             else:
#                 print(f'#{test_case} N')
#         else:
#             print(f'#{test_case} N')
#
#     print(len(Q), sht_len)
# T = int(input())
#
# for test_case in range(1, T + 1):
#     P, Q = input().split()[0], input().split()[0]
#
#     if P == Q:
#         print(f'#{test_case} N')
#         continue
#
#     sht_len = min(len(P),len(Q))
#
#     for i in range(sht_len):
#         if P[i] != Q[i]:
#             print(f'#{test_case} Y')
#             break
#
#     else:
#         if Q[sht_len] != 'a':
#             print(f'#{test_case} Y')
#         else:
#             print(f'#{test_case} N')

