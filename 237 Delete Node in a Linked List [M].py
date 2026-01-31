# linked list


class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def __init__(self, node):
        self.node = node


def deleteNode(node):
    while node.next.next != None:
        node.val = node.next.val
        node = node.next
    node.val = node.next.val
    node.next = None


s = Solution(ListNode(4, ListNode(5, ListNode(1, ListNode(9, None)))))
deleteNode(s.node.next)  # Delete node with value 5
current = s.node
while current:
    print(current.val, end=" ")
    current = current.next
