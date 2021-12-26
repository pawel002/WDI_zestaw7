class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def delete_divisors(head: Node):
    p = Node(0)
    p.next = head
    flag = True
    while p.next is not None:
        if p.next.next.val % p.next.val == 0:
            if p.next.next is None:
                p.next = None
            else:
                p.next = p.next.next
        if flag:
            Head = p.next
            flag = False
        p = p.next
    return Head


# Prints linked list
def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


A = Node(4)
B = Node(16)
C = Node(5)
D = Node(135)
A.next = B
B.next = C
C.next = D
node_printer(delete_divisors(A))
