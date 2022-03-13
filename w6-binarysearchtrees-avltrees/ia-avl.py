def is_avl(bst):
    # Determine whether this bst is AVL balanced or not.
    root = bst.root
    return rec_is_avl(bst, root)
    
def rec_is_avl(bst, root):
    if root is None:
        return True
    leftside = r_height(bst, root.left)
    rightside = r_height(bst, root.right)
    if (abs(leftside - rightside) <= 1) and rec_is_avl(bst, root.left) is True and rec_is_avl(bst, root.right) is True:
        return True
    return False

def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))
