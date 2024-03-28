import sys
sys.stdin = open("input.txt", "r")

for i in range(1,int(input())+1):P, Q, R, S, W = map(int,input().split());print(f'#{i} {min(W*P,Q + max(0,(W-R)*S))}')
