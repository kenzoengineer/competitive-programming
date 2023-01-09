# Tree, DFS

test = [1, None, 2, 3]
def preorderTraversal(root):
    res = []
    def recurse(node):
        if node is None:
            return
        res.append(node.val)
        recurse(node.left)
        recurse(node.right)
    recurse(root)
    return res

print(preorderTraversal(test))