import sys
sys.stdin = open("input.txt", "r")


for i in range(int(input())):
    print(f"#{i+1}", int(input())//3)