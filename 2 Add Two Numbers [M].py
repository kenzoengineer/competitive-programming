# Linked List
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return str(self.val)
        
t_l1 = ListNode(2,ListNode(4,ListNode(3,None)))
t_l2 = ListNode(5,ListNode(6,ListNode(4,None)))

def addTwoNumbers(l1, l2):
    def add(n1,n2,carry):
        if (n1 is None and n2 is None):
            return None if carry == 0 else ListNode(1,None)
        if (n2 is None):
            return ListNode((n1.val + carry)%10, add(n1.next, None, (n1.val + carry)//10))
        if (n1 is None):
            return ListNode((n2.val + carry)%10, add(None, n2.next, (n2.val + carry)//10))
        return ListNode((n1.val + n2.val + carry)%10, add(n1.next, n2.next, (n1.val + n2.val + carry)//10))
    return add(l1,l2,0)

print(addTwoNumbers(t_l1,t_l2))
