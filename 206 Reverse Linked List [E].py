# Recursion, linked list

def reverseList(head):

    # iterative
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

    # recursive
    def recurse(node):
        if node is None or node.next is None:
            return node
        next = recurse(node.next)
        node.next.next = node
        node.next = None
        return next
    return recurse(head)