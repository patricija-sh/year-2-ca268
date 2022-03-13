def rotation_type(bst):
    left = bst.r_height(bst.root.left)
    if left == 2:
        if bst.root.left != None:
            left_leftroot = bst.r_height(bst.root.left.left)
            if left_leftroot == 1:
                return "ll"
            left_rightroot = bst.r_height(bst.root.left.right)
            if left_rightroot == 1:
                return "lr"
    #right subtree
    right = bst.r_height(bst.root.right)
    if right == 2:
        if bst.root.right != None:
            right_rightroot = bst.r_height(bst.root.right.right)
            if right_rightroot == 1:
                return "rr"
            right_leftroot = bst.r_height(bst.root.right.left)
            if right_leftroot == 1:
                return "rl"
