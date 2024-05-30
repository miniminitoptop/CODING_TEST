# def fun(n):
#     fibList = [1, 1]
#     if n == 1 or n == 2:
#         return 1
#     for i in range(2, n):
#         fibList.append(fibList[i - 1] + fibList[i - 2])
#     return fibList
#
#
# a = fun(20)
# print(a)

F1 = 0
F2 = 1
mnt = 0

for i in range(1,50):
    mnt = F2
    F2 = F1 + F2
    F1 = mnt

    print(F1,F2)

