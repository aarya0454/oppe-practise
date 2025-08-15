def _dfs_adj_mat(matrix,node,visited):
    visited[node]=True
    for i in range(len(matrix)):
        if matrix[node][i] == 1 and not visited[i]:
            _dfs_adj_mat(matrix,i,visited)
def dfs_adj_mat(matrix,start):
    visited = [False]*len(matrix)
    _dfs_adj_mat(matrix,start,visited)
    return visited

def _dfs_adj_lst(a_list,node,visited,parent):
    visited[node]=True
    for v in a_list[node]:
        if not visited[v]:
            parent[v]=node
            _dfs_adj_lst(a_list,v,visited,parent)
def dfs_adj_lst(a_list,start):
    visited = {i:False for i in a_list}
    parent = {i:-1 for i in a_list}
    parent[start] = start
    _dfs_adj_lst(a_list,start,visited,parent)
    return visited,parent



def dfs_pre_post_utils(a_list,node,visited,pre,post,count,edges):
    visited[node] = True
    pre[node] = count
    count+=1
    for v in a_list[node]:
        if not visited[node]:
            edges.add((node,v))
            dfs_pre_post_utils(a_list,v,visited,pre,post,count,edges)
    post[node] = count
    count +=1





def dfs_pre_post(a_list,start):
    visited = {i:False for i in a_list}
    pre = {i:0 for i in a_list}
    post = {i:0 for i in a_list}
    count =1
    edges = {}
    dfs_pre_post_utils(a_list,start,visited,pre,post,count,edges)
    return visited,pre,post,edges

def cycle_detection(a_list):
    visited,pre,post,edges = dfs_pre_post(a_list,1)
    for u in a_list:
        for v in a_list[u]:
            if pre[u]<pre[v] and post[u]>post[v] and (u,v) not in edges:
                return True
    return False