import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    lst = [0]*N
    stu_tot = 0

    for i in range(1, N+1):
        F, M, P = map(int,input().split())
        lst[i-1] = ((F/100)*35+(M/100)*45+(P/100)*20)

        if i == K:
            stu_tot = lst[i-1]

    lst2 = sorted(lst, reverse=True)

    per = (lst2.index(stu_tot)/N)*100

    if 0 <= per and per < 10 :
        print(f"#{test_case} A+")
    elif 10 <= per and per < 20 :
        print(f"#{test_case} A0")
    elif 20 <= per and per < 30 :
        print(f"#{test_case} A-")
    elif 30 <= per and per < 40:
        print(f"#{test_case} B+")
    elif 40 <= per and per < 50:
        print(f"#{test_case} B0")
    elif 50 <= per and per < 60:
        print(f"#{test_case} B-")
    elif 60 <= per and per < 70:
        print(f"#{test_case} C+")
    elif 70 <= per and per < 80:
        print(f"#{test_case} C0")
    elif 80 <= per and per < 90:
        print(f"#{test_case} C-")
    elif 90 <= per and per < 100:
        print(f"#{test_case} D0")





    # print((lst2.index(stu_tot)/N)*100)


