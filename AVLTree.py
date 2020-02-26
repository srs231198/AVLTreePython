import AVLNode
import Book


class AVLTree(object):

    def getHeight(self, node):
        if node is None:
            return -1

        return node.height
    
    def getBalance(self, node):
        if node is None:
            return -1
        
        return self.getHeight(node.left_ptr) - self.getHeight(node.right_ptr)
    
    def InOrder(self, root):
        if root is None:
            return
        
        self.InOrder(root.left_ptr)
        print("{0} ".format(root.val), end="")
        self.InOrder(root.right_ptr)