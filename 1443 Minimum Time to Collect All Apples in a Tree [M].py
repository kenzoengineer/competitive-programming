# Tree, DFS

t_1 = 7
t_2 = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
t_3 = [False, False, True, False, True, True, False]
def minTime(n, edges, hasApple):
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    def dfs(node, parent):
        res = 0
        for child in adj[node]:
            if child == parent:
                continue
            child_amount = dfs(child, node)
            if child_amount > 0 or hasApple[child]:
                res += child_amount + 2
        return res
    return dfs(0, None)

print(minTime(t_1, t_2, t_3))
