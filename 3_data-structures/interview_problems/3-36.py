'''
[4] Write a function to find the middle node of a singly linked list.
'''
'''
thought:
- create 2 pointers.
    - 1 will be 2x speed of the other.
- odd e.g. LL of length 7.
        fast -1 1 3 5 break
        slow 0  1 2 3 break

- even e.g. LL of length 8.
        fast -1 1 3 5 7 break
        slow 0  1 2 3 4 break

- NOTE: my implemntation takes the 2nd value as the middle for even-lengthed lists.
'''
from helpers import LinkedList

def get_middle_node(head):

    ptr = head
    
    slow = ptr
    fast = ptr

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(f"middle val is {slow.val}")
    return slow

# Driver code.
if __name__ == "__main__":

    # create singly linked list example.
    eg1 = LinkedList()
    eg1.build_list(6)
    eg1.print_list()

    get_middle_node(eg1.head)

    eg1.build_list(5)
    eg1.print_list()
    get_middle_node(eg1.head)

    eg1.build_list(9)
    eg1.print_list()
    get_middle_node(eg1.head)