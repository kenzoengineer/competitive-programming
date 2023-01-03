# BFS

test = [1, 2, 3, None, 5, None, 4]
def rightSideView(root):
    if not root:
        return []
    res = []
    queue = [[root]]
    while queue[0] != []:
        queue.append([])
        nodes = queue.pop(0)
        res.append(nodes[0].val)
        for n in nodes:
            if n.right:
                queue[-1].append(n.right)
            if n.left:
                queue[-1].append(n.left)
    return res


print(rightSideView(test))
