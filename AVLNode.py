import Book


class AVLNode:
    def __init__(self, key, val, height):
        # Initialize the node with the string key, book object val 
        # and the int height
        self.key = key
        self.val = val
        self.height = height
        # set the left and right ptr's to null
        self.left_ptr = None
        self.right_ptr = None

    def set_left_ptr(self, node):
        self.left_ptr = node

    def set_right_ptr(self, node):
        self.right_ptr = node
