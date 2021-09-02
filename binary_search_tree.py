class Node:

    # I am even letting the 'None' data
    # to be entered into a node.
    def __init__(self, data=None):
        self.data = data
        self.left_ptr = None
        self.right_ptr = None


class BinarySearchTree:

    def __init__(self):
        self.ptr_to_root = None


    def insert(self, data):
        '''
        This feature/function helps the users to insert data into a Binary 
        Search Tree.
        '''
        # To insert, the first thing we have to do is
        # creating a node :-
        node = Node(data)
        
        # We create a temperory pointer as we
        # won't move ptr_to_root.
        temp_ptr = self.ptr_to_root

        # CASE 1 > If ptr_to_root is None i.e. If BST
        # is empty :
        if temp_ptr == None:
            temp_ptr = node
            self.ptr_to_root = node
        

        # CASE 2 > If BST is not empty already : 
        while temp_ptr != None:
             
            # Below is the pointer which will remain behind
            # temp_ptr by one step.
            r = temp_ptr
            
            # If we already have the data present in BST, we
            # cannot re-enter it. Hence, we simply exit the 
            # function.
            if data == temp_ptr.data:
                return
            
            # If the data is having lesser value then temp_ptr's data, 
            # then we move the temp_ptr to its left, or else the right.
            if data < temp_ptr.data:
                temp_ptr = temp_ptr.left_ptr
            else:
                temp_ptr = temp_ptr.right_ptr
        
        # r is the tail pointer, which follows the temp_ptr. 
        # Eventually, we will compare if the value that we wanrt to insert
        # is less or more then r.data, and accordingly insert the data desired.
        if data < r.data:
            r.left_ptr = node
        else:
            r.right_ptr = node

    

    def search(self, data):
        
        # If the BST is empty, then we do not 
        # have the element present in the BST for sure:
        temp_ptr = self.ptr_to_root
        
        # If BST is empty, then :
        if temp_ptr == None:
            return None

        
        # If BST is not empty, we may or may not be 
        # finding the element in the tree :
        while temp_ptr != None:

            if data == temp_ptr.data:
                return temp_ptr
            
            elif data < temp_ptr.data:
                temp_ptr = temp_ptr.left_ptr
            
            else:
                temp_ptr = temp_ptr.right_ptr
        
        # If the element is not present in BST :
        return None


        
            
    def search_recursive(self, ptr_to_root, data):

        temp_ptr = ptr_to_root

        if temp_ptr == None:
            return None

        else:
            while temp_ptr != None:

                if data == temp_ptr.data:
                    return temp_ptr

                elif data < temp_ptr.data:
                    return self.search_recursive(temp_ptr.left_ptr, data) 
                
                else:
                    return self.search_recursive(temp_ptr.right_ptr, data)
        
        return None

    
    def insert_recursive(self, ptr_to_root, data):
        
        node = Node(data)
        temp_ptr = ptr_to_root
        
        # If BST is empty :
        if temp_ptr == None:
            temp_ptr = node
        
        # Else if BST is not empty:
        if data < temp_ptr.data:
            if temp_ptr.left_ptr == None:
                temp_ptr.left_ptr = node
            else:
                self.insert_recursive(temp_ptr.left_ptr, data)
        elif data > temp_ptr.data:
            if temp_ptr.right_ptr == None:
                temp_ptr.right_ptr = node
            else:
                self.insert_recursive(temp_ptr.right_ptr, data)
        else: # If data is already present in BST,
            return

    
    # def inOrderTravsersal(self, self.ptr_to_root):
    #     inOrder_list = []
    #     if self.ptr_to_root:
    #         inOrderTraversal(self.ptr_to_root.left_ptr)
    #         inOrder_list.append(self.ptr_to_root.data)
    #         inOrderTraversal
    #     return inOrder_list
                
        

# Testing :-


b1 = BinarySearchTree()

b1.insert(5)

b1.insert(7)


# search_result = b1.search(5)

# print(search_result)

