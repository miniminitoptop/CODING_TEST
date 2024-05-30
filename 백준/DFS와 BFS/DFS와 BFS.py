import sys
sys.stdin = open("input.txt", "r")

# N, M, V = map(int, input().split())
# def dfs(f, visit, ls):
#
#     ls[f].sort()
#     ls1 = []
#
#     for j in ls[f]:
#
#         if j in visit:
#             continue
#
#         else:
#             visit.append(j)
#             ls1.append(j)
#             dfs(j, visit, ls)
#             break
#
#     if not ls1:
#         return
#
# def bfs(f, visit, ls):
#
#     ls[f].sort()
#     ls1 = []
#
#     for j in ls[f]:
#
#         if j in visit:
#             continue
#
#         visit.append(j)
#         ls1.append(j)
#
#     if not ls1:
#         return
#
#     else:
#         for k in ls1:
#             bfs(k, visit, ls)
#
#
# lst = list([] for _ in range(N+1))
#
# v1, v2 = [V], [V]
#
# for i in range(M):
#     X, Y = map(int, input().split())
#     lst[X].append(Y)
#     lst[Y].append(X)
#
# dfs(V, v1, lst)
# bfs(V, v2, lst)
#
# ans1 = " ".join(list(map(str,v1)))
# ans2 = " ".join(list(map(str,v2)))
#
# print(ans1)
# print(ans2)

N, M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)






