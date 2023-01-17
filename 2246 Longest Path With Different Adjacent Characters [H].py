# Array, Tree, DFS

t_1 = [-1,0,0,1,1,2]
t_2 = "abacbe"
def longestPath(parent, s):
    graph = [[] for _ in range(len(parent))]
    ans = 0
    # make the adj list
    for i in range(len(parent)):
        if parent[i] != -1:
            graph[parent[i]].append(i)
    print(graph)
    def dfs(node):
        nonlocal ans

        # keep track of longest 2 and dfs
        longest_1 = 0
        longest_2 = 0
        for n in graph[node]:
            length = dfs(n)
            # if their characters arent the same
            if s[node] != s[n]:
                if length > longest_1:
                    longest_2 = longest_1
                    longest_1 = length
                elif length > longest_2:
                    longest_2 = length
        ans = max(ans, longest_1 + longest_2 + 1)
        return longest_1 + 1
    
    dfs(0)
    return ans

print(longestPath(t_1,t_2))