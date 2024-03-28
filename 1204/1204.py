import sys
sys.stdin = open("input.txt", "r")

# for test_case in range(1, int(input()) + 1):
#     K = int(input())
#     lst = list(map(int,input().split()))
    
#     dic = {}
#     for i in range(0,101):
#         dic[i] = lst.count(i)
    
#     bst = max(dic.values())
#     dic = dict(sorted(dic.items(), key=lambda x:x[1],reverse=True))
    
#     bstk = 0
    
#     for key, value in dic.items():
        
#         if value != bst:
#             break
        
#         if key > bstk:
#             bstk = key
        
#     print(f'#{test_case} {bstk}')

lst = []

for t in range(int(input())):
     n,d=input(),input().split()
     lst.append(f'#{n} {max(d,key=d.count)}')
    
for j in range(len(lst)):
    print(lst[j])