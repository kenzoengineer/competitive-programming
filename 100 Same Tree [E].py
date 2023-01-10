# Tree, BFS

test1 = [1,2,3]
test2 = [1,2,3]

def isSameTree(p, q):
    def recurse(t1, t2):
        if t1 is None and t2 is None:
            return True
        elif (t1 is None and t2 is not None) or (t1 is not None and t2 is None):
            return False
        return t1.val == t2.val and recurse(t1.left, t2.left) and recurse(t1.right, t2.right)
    return recurse(p,q)

print(isSameTree(test1,test2))