class Node:

    def __init__(self, data, left_ptr, right_ptr):
        self.key = data
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

class BinarySearchTree:

    def __init__(self, ptr_to_root = None):
        self.ptr_to_root

    def insert(self, data):
        # To insert, the first thing we have to do is
        # creating a node :-
        node = Node()
        # If ptr_to_root is empty :
        if not self.ptr_to_root:
            self.ptr_to_root = node
        
        
