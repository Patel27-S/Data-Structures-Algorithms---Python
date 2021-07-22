from linked_list import Node

# Implementing a Stack using 'LinkedList'.

class Stack(Node):


    def __init__(self,top_ptr = None):
        self.top_ptr = top_ptr


    # Adding the default value of 'None' in the below method,
    # lets a user insert even a node with no-value in the Stack.
    def push(self, data=None):
        '''
        This method will push the element onto Stack.
        '''
        # When we have to push, first thing that we need
        # to do is making a node. And, storing the data into it
        node = Node(data = data)

        # If the stack is empty, then we have to put the Node's
        # instance into it.
        if self.top_ptr == None:
            self.top_ptr = node

        # If the top_ptr is not None/stack isn't empty.
        else:
            node.next = self.top_ptr
            self.top_ptr = node
        # Time Complexity for push() operation above is O(1).


    def pop(self):
        '''
        This method will pop the top most element of the stack/ the most recently
        pushed element of the stack/ the node that is stored in top_ptr.
        '''
        # Verifying the empty stack case :-
        if self.top_ptr == None:
            print('The stack is empty.')
            return

        # Now, the stack is not empty.
        else:
            temp_ptr = self.top_ptr
            self.top_ptr = self.top_ptr.next
            temp_ptr = None
        # Time Complexity for pop() function is O(1).


    def peek(self, index):
        '''
        This method shows the data at a particular index in a Stack.
        '''
        temp_ptr = self.top_ptr
        count = 1
        while count != index:
            temp_ptr = temp_ptr.next


    def length(self):
        '''
        This method returns the length of a Stack.
        '''
        count = 0
        temp_ptr = self.top_ptr
        while temp_ptr != None:
            count += 1
            temp_ptr = temp_ptr.next
        return count
        # Time Complexity of length() is O(n).





    def display(self):
        '''
        This method will display the Stack data structure.
        '''
        # In this display() function we'll print the data of top_ptr,
        # and then move to its next node and repeat until top_ptr != None.
        while self.top_ptr != None:
            print(self.top_ptr.data)
            print('||')
            self.top_ptr = self.top_ptr.next
        # Time Complexity of display() function is O(n).


# Testing :-

s1 = Stack()
s1.push('Smit')
s1.push('Hari Bhakto')
s1.push('Dayalu Swami')
s1.push('Guruji')
s1.push('Maharaj')

s1.pop()
s1.pop()

print('The length of Stack is {}'.format(s1.length()))
s1.display()
