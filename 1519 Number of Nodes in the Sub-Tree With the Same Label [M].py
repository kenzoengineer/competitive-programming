# Tree, DFS

t_1 = 7
t_2 = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
t_3 = "abaedcd"
def countSubTrees(n, edges, labels):
    graph = [[] for _ in range(n)]
    res = [0] * n
    counts = [0] * 26
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    def dfs(node, parent):
        index = ord(labels[node]) - 97
        old = counts[index]
        counts[index] += 1

        for child in graph[node]:
            if child != parent:
                dfs(child, node)
        res[node] = counts[index] - old
    
    dfs(0,None)
    return res

print(countSubTrees(t_1,t_2,t_3))