from Node import Node

#
#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(r_height(self, ptr.left), r_height(self, ptr.right))

def rotation_type(bst):
    left = r_height(bst, bst.root.left)
    right = r_height(bst, bst.root.right)
    #print("root =", bst.root)
    if left == right:
        return None
    #right subtree
    elif bst.root.right != None and bst.root.left == None:
        return bst.root
    #elif abs(right) - abs(left) > 1:
    #    return bst.root
    elif right > left:
        if bst.root.right != None:
            if bst.root.right.right != None and bst.root.right.left == None:
                return bst.root.right
            #print("right =", bst.root.right)
            right_rightroot = r_height(bst, bst.root.right.right)
            #print("rightright =", bst.root.right.right)
            right_leftroot = r_height(bst, bst.root.right.left)
            #print("rightleft =", bst.root.right.left)
            if right_rightroot > right_leftroot:
                return bst.root.right.right
            else:
                return bst.root.right
    elif left > right:
        if bst.root.left != None:
            if bst.root.left.right != None and bst.root.left.left == None:
                return bst.root.left
            #print("left =", bst.root.left)
            left_leftroot = r_height(bst, bst.root.left.left)
            #print("leftleft =", bst.root.left.left)
            left_rightroot = r_height(bst, bst.root.left.right)
            #print("leftright =", bst.root.left.right)
            if left_leftroot + 1 < left_rightroot:
                return bst.root.left.left
            elif left_leftroot - 1 > left_rightroot:
                return bst.root.left
            else:
                return None

def add(tree, item):
    """ Add this item to its correct position on the tree """
    # This is a non recursive add method. A recursive method would be cleaner.
    if tree.root == None: # ... Empty tree ...
        tree.root = Node(item, None, None) # ... so, make this the root
    else:
        # Find where to put the item
        child_tree = tree.root
        while child_tree != None:
            parent = child_tree
            if item < child_tree.item: # If smaller ... 
                child_tree = child_tree.left # ... move to the left
            elif item > child_tree.item:
                child_tree = child_tree.right

        # child_tree should be pointing to the new node, but we've gone too far
        # we need to modify the parent nodes
        if item < parent.item:
            parent.left = Node(item, None, None)
        elif item > parent.item:
            parent.right = Node(item, None, None)
        # Ignore the case where the item is equal.
        return rotation_type(tree)
        
    #
    #   Note that you can get the height of a node by calling tree.recurse_height().
    #       For example, the height of the root is tree.recurse_height(tree.root)
    #
