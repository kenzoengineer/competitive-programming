# Tree, Union find

import math
def numberOfGoodPaths(vals, edges):   
    res = 0
    # create an adjacency list
    graph = [[] for _ in range(len(vals))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # create a sorted dictionary of values to nodes[]
    val_assignments = dict()
    for i in range(len(vals)):
        if vals[i] in val_assignments:
            val_assignments[vals[i]].append(i)
        else:
            val_assignments[vals[i]] = [i]
    keys = list(val_assignments.keys())
    keys.sort()
    sorted_vals = {i: val_assignments[i] for i in keys}
    val_assignments = sorted_vals

    # union find datastructure
    # [1,2,...,n - 1]
    parent = [i for i in range(len(vals))]
    rank = [0] * len(vals)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xSet = find(x)
        ySet = find(y)
        if xSet == ySet:
            return
        elif rank[xSet] < rank[ySet]:
            parent[xSet] = ySet
        elif rank[xSet] > rank[ySet]:
            parent[ySet] = xSet
        else:
            parent[ySet] = xSet
            rank[xSet] += 1
    
    # iterate over all nodes
    # k = 1, v = 0, 3, etc.
    for k in val_assignments:
        for v in val_assignments[k]:
            if graph[v] == []:
                continue
            for neighbour in graph[v]:
                if vals[v] >= vals[neighbour]:
                    union(v, neighbour)
        group = dict()
        for u in val_assignments[k]:
            if find(u) in group:
                group[find(u)] += 1
            else:
                group[find(u)] = 1
        
        for g in group:
            res += group[g] * ((group[g] + 1) / 2)

    return math.floor(res)