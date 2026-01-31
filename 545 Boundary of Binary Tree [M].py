# DFS, Binary Tree


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boundary_of_binary_tree(root):
    # left
    lb = [root.val]
    curr = root.left
    while curr is not None:
        lb.append(curr.val)
        # ignore last leaf
        if not curr.left and not curr.right:
            lb.pop()
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

    # right
    rb = []
    curr = root.right
    while curr is not None:
        rb.append(curr.val)
        if not curr.left and not curr.right:
            rb.pop()
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left

    # boundary
    b = []
    stack = [root]
    while len(stack):
        curr = stack.pop(-1)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        if not curr.right and not curr.left:
            b.append(curr.val)

    print(lb, b, rb)
    return lb + b + rb[::-1]


r = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4)))
print(boundary_of_binary_tree(r))
