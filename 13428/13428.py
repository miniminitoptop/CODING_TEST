import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = list(input())
    min_val = max_val = int("".join(N))
    min_ans = max_ans = "".join(N)

    for i in range(len(N)):

        for j in range(i+1, len(N)):
            N[i], N[j] = N[j], N[i]

            if int("".join(N)) >= max_val:
                max_val = int("".join(N))
                max_ans = "".join(N)

            elif N[0] != "0" and int("".join(N)) <= min_val:
                min_val = int("".join(N))
                min_ans = ("".join(N))

            N[i], N[j] = N[j], N[i]

    print(f"#{test_case} {min_ans} {max_ans}")

