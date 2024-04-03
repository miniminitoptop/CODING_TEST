import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = []

    lst.append(N // 50000)
    lst.append((N % 50000) // 10000)
    lst.append((N % 10000) // 5000)
    lst.append((N % 5000) // 1000)
    lst.append((N % 1000) // 500)
    lst.append((N % 500) // 100)
    lst.append((N % 100) // 50)
    lst.append((N % 50) // 10)

    print(f"#{test_case}")
    print(" ".join(list(map(str, lst))))