import sys
sys.stdin = open("input.txt", "r")

# print(" ".join(map(str,list(i for i in range(int(input()),-1,-1)))))

print(*range(int(input()),-1,-1))