'''
Implement an algorithm to reverse a linked list. Now do it without recursion.
'''
# Helper classes and functions.
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def build_linked_list(size):
    head = Node(None)
    ptr = head
    for i in range(size):
        to_insert = Node(i)
        ptr.next = to_insert
        ptr = ptr.next

    return head.next

def print_linked_list(head):
    print("Linked list values:")

    ptr = head

    while ptr:
        print(ptr.val)
        ptr = ptr.next

# Iterative implemntation.
def reverse_ll_iterative(head):
    ptr = head
    prev = None

    while ptr:

        orig_next = ptr.next
        ptr.next = prev
        prev = ptr
        ptr = orig_next
    
    return prev

# TODO: Recursive implementation.
def reverse_ll_recursive():
    pass

# Driver code.
if __name__ == "__main__":

    # build linked list.
    eg1 = build_linked_list(6)

    print_linked_list(eg1)

    reversed_eg1 = reverse_ll_iterative(eg1)

    print_linked_list(reversed_eg1)





    
