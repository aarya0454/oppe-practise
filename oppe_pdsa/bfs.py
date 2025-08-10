from collections import deque

def bfs_adjc_mat(mat,start):
    queue = deque()
    visited = [False]*len(mat)
    queue.append(start)
    visited[start] = True
    while len(queue)>0:
        node = queue.popleft()
        for i in range(mat[node]):
            if mat[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i]=True
    return visited

def bfs_adj_list(a_list,start):
    queue = deque()
    visited = {i:False for i in a_list}
    level = {i:-1 for i in a_list}
    parent = {i:-1 for i in a_list}
    queue.append(start)
    visited[start] = True
    parent[start] = start
    level[start] = 0
    while len(queue)>0:
        node = queue.popleft()
        for v in a_list[node]:
            if not visited[v]:
                queue.append(v)
                parent[v] = node
                level[v] = level[node]+1
                visited[v] = True
    return visited,level,parent

