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
