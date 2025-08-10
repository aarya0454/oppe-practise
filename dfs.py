def _dfs_adj_mat(matrix,node,visited):
    visited[node]=True
    for i in range(len(matrix)):
        if matrix[node][i] == 1 and not visited[i]:
            _dfs_adj_mat(matrix,i,visited)
def dfs_adj_mat(matrix,start):
    visited = [False]*len(matrix)
    _dfs_adj_mat(matrix,start,visited)
    return visited