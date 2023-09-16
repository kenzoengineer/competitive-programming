# Binary search tree,

def lowestCommonAncestor(root, p, q):
    # l is the smallest
    l = min(p.val,q.val)
    r = max(p.val,q.val)
    curr = root
    while curr.val != l and curr.val != r:
        if curr.val >= l and curr.val <= r:
            return curr
        elif curr.val >= l and curr.val >= r:
            curr = curr.left
        else:
            curr = curr.right
    return curr