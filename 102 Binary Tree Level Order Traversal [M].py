# BFS

test = [3, 9, 20, None, None, 15, 7]
def levelOrder(root):
    res = []
    if not root:
        return res
    stack = [[root]]
    while len(stack) > 0:
        next = stack.pop(0)
        if next:
            stack.append([])
            res.append([])
            for n in next:
                if n.left:
                    stack[-1].append(n.left)
                if n.right:
                    stack[-1].append(n.right)
                res[-1].append(n.val)
    return res


print(levelOrder(test))
