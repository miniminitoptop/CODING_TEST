import sys
sys.stdin = open("input.txt", "r")

T = input()
lst = []

for i in T:
    lst.append(ord(i)-64)

print(" ".join(map(str, lst)))