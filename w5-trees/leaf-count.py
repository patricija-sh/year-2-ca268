class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

    def count_leaves(self):
        return self.rec_count_leaves(self.root)
    
    def rec_count_leaves(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return self.rec_count_leaves(root.left) + self.rec_count_leaves(root.right)
