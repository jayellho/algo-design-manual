'''
[4] Write a program to convert a binary search tree into a linked list.
'''
from helpers import BST, inorder, Node

def get_linked_list(bst, node):

    if not bst:
        return node
    node = get_linked_list(bst.left, node)
    node.next = Node(bst.val)
    node = node.next
    node = get_linked_list(bst.right, node)

    return node
    
def bstToLinkedList(bst):

    res = Node(None)
    ptr = res

    get_linked_list(bst, ptr)    
    return res.next


# Driver code.
if __name__ == "__main__":

    sorted_list = list(range(8))
    bst = BST(sorted_list)

    linked_list = bstToLinkedList(bst.root)

    ptr = linked_list

    while ptr:
        print(ptr.val)
        ptr = ptr.next

    inorder(bst.root)
