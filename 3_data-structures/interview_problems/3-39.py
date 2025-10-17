'''
Implement an algorithm to reverse a linked list. Now do it without recursion.
'''
from helpers import LinkedList
# Iterative implementation.
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
    ll = LinkedList()
    # build linked list.
    ll.build_list(6)

    eg1 = ll.head

    ll.print_list()

    ll.head = reverse_ll_iterative(eg1)

    ll.print_list()





    
