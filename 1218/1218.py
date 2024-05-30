import sys
sys.stdin = open("input.txt", "r")

for T in range(1,11):
    N = int(input())
    lst = list(input())

    lst1 = {")" : "(", "]" : "[", "}" : "{", ">" : "<"}

    stack = []
    ans = 1

    for i in lst:
        if i == "(" or i == "[" or i == "{" or i == "<":
            stack.append(i)

        else:
            if lst1[i] in stack:
                stack.pop(stack.index(lst1[i]))

            else:
                ans = 0
                break

    if len(stack) >= 1:
        ans = 0

    print(ans)











