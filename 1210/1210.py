import sys
sys.stdin = open("input.txt", "r")


def fds(ls, n):

    global st1
    global st2

    if st2 + n < 0 or st2 + n > 99 or lst[st1][st2+n] == 0:
        return

    else:
        st2 += n
        fds(ls, n)


for test_case in range(1, 11):

    T = int(input())
    lst = [list(map(int, input().split()))for _ in range(100)]

    st1 = 99
    st2 = lst[99].index(2)

    while st1 != 0:

        if (st2 - 1) > 0 and lst[st1][st2 - 1] == 1:
            fds(lst, -1)
            st1 -= 1
            continue

        if (st2 + 1) < 99 and lst[st1][st2 + 1] == 1:
            fds(lst, 1)
            st1 -= 1
            continue

        st1 -= 1

    print(f"#{test_case}", st2)







