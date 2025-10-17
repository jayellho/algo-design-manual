# Helper classes and functions.
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class BinTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    # builds a linked list of self.size with arbitrarily increasing numbers.
    def build_list(self,size):
        ptr = self.head
        for i in range(size):
            to_insert = Node(i)
            ptr.next = to_insert
            ptr = ptr.next
        self.head = self.head.next
    
    def print_list(self):
        print("Linked list values: ")
        ptr = self.head
        
        while ptr:
            print(ptr.val)
            ptr = ptr.next


# Traversals of trees.
def inorder(node):

    if not node:
        return
    inorder(node.left)
    print(node.val, end = " ")
    inorder(node.right)

class BST:
    def __init__(self, sorted_list):
        self.root = self._build_bst(sorted_list)

    
    def _build_bst(self, sorted_list):
        n = len(sorted_list)

        if n <= 0:
            return
        mid = n // 2

        node = BinTreeNode(sorted_list[mid])
        node.left = self._build_bst(sorted_list[:mid])
        node.right = self._build_bst(sorted_list[mid+1:])

        return node



