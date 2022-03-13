class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for item in lst:
                self.add(item)

    # Non recursive add method, easier to work out the path to the parent        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            forward_list = []
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ...
                    forward_list.append(child_tree.item)
                    child_tree = child_tree.left # ... move to the left
                else:
                    forward_list.append(child_tree.item)
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)
            back_list = []
            for i in range(len(forward_list)):
                back_list.append(forward_list[-i - 1])
            return back_list
