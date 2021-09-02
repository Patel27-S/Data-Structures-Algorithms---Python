# In this approach of coding a BST datastructure,
# We have not used a Separate Node class and a Datastructure class with
# a head_ptr. But, we have a BSTNode and that is it to go with.



class BinarySearchTree:
    # We are defining the constructor such that it just creates a simple node.
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    
    def add_child(self, value):
        '''Recursive procedure for inserting a node in BST.'''

        if value == self.value:
            return

        if value < self.value:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinarySearchTree(value)

        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinarySearchTree(value)
        # The Time Complexity and Space Complexity for the above function are :
        # O(height of BST) to be strict, for both.
    
    
    def inorder_traversal(self):
        array = []
        if self.left:
            array += self.left.inorder_traversal()
        array.append(self.value)
        if self.right:
            array += self.right.inorder_traversal()
        return array
        # The Time Complexity for the above function is : O(n)
        # Space Complexity for the above function is : O(n) as well.


    def pre_order_traversal(self):
        array = []
        array.append(self.value)
        if self.left:
            array += self.left.pre_order_traversal()
        if self.right:
            array += self.right.pre_order_traversal()
        return array
        
    

    def post_order_traversal(self):
        array = []
        if self.left:
            array += self.left.post_order_traversal()
        if self.right:
            array += self.right.post_order_traversal()
        array.append(self.value)

        return array


    def search(self, value):

        if value == self.value:
            return 'Value is found'
        elif value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
        return False

def build_tree(array):
    root = BinarySearchTree(array[0])
    for i in range(1, len(array)):
        root.add_child(array[i])
    
    return root

    

if __name__ == '__main__':
    numbers = [1,2,4.5,4,7,6]

    a = build_tree(numbers)

    print(a.inorder_traversal())
    print(a.post_order_traversal())
    print(a.pre_order_traversal())

    print(a.search(7.1))

