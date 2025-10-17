'''
[4] Write a function to determine whether two binary trees are identical. 
Identical trees have the same key value at each position and the same structure.
'''

from helpers import BinTreeNode

# TODO: refactor tree building logic.

def isSameTree(node1, node2):

    if not node1 and not node2:
        return True
    
    if not node1 or not node2:
        return False
    

    if node1.val != node2.val:
        return False
    
    return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)



# Driver code.
if __name__=="__main__":

    tree = BinTreeNode(1)
    tree.left = BinTreeNode(2)
    tree.right = BinTreeNode(3)
    tree.left.left = BinTreeNode(4)
    tree.left.right = BinTreeNode(5)
    tree.right.left = BinTreeNode(6)
    tree.right.right = BinTreeNode(7)


    tree2 = BinTreeNode(1)
    tree2.left = BinTreeNode(2)
    tree2.right = BinTreeNode(3)
    tree2.left.left = BinTreeNode(4)
    tree2.left.right = BinTreeNode(5)
    tree2.right.left = BinTreeNode(6)
    tree2.right.right = BinTreeNode(7)

    res = isSameTree(tree, tree2)
    print(res)