# BFS

test = [3, 9, 20, None, None, 15, 7]
def minDepth(root):
    queue = [[root]]
    res = 0
    if not root:
        return 0
    while queue:
        nodes = queue.pop(0)
        res += 1
        queue.append([])
        for node in nodes:
            if node.left == node.right and node.left == None:
                return res
            if node.left:
                queue[-1].append(node.left)
            if node.right:
                queue[-1].append(node.right)
    return res
