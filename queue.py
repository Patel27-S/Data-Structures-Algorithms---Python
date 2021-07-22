class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(Node):


    # As soon as we instantiate Queue,
    # we're having an empty queue_ptr.
    def __init__(self):
        self.queue_ptr = None


    def insert(self, data):
        '''
        This methods inserts an element in a queue.
        '''
        # First, thing that we want to do is,
        # creating a node with data=data, as we want to insert a node.
        node = Node(data = data)

        # Case 1 :- If the self.queue_ptr is empty,
        # meaning, there're no elements in a queue :
        if self.queue_ptr == None:
            self.queue_ptr = node

        # Case 2 :- If the self.queue_ptr isn't empty
        # meaning, there're elements in the queue already:
        node.next = self.queue_ptr
        self.queue_ptr = node

        # Time Complexity of insert() operation is O(1).

    def delete(self):
        '''
        This method deletes/dequeues from a queue.
        '''

        temp_ptr = self.queue_ptr

        # Idea :- The idea is to traverse the temp_ptr all the way
        # until the second last node and then  make its next as None.
        # We need to know the length of the linkedlist for this operation :

        count = 0
        while temp_ptr:
            temp_ptr = temp_ptr.next
            count += 1
        # The count's value now will provide the length of linkedlist.

        # We're bringing the temp_ptr back to the initial position :
        temp_ptr = self.queue_ptr

        while count-2:
            count -= 1
            temp_ptr = temp_ptr.next

        temp_ptr.next = None

        # Time Complexity of delete() operation is O(n).


    def length(self):
        '''
        This method returns the length of a queue.
        '''

        # We are setting the counter variable as 0.
        queue_length = 0

        # We are setting a temp_ptr at self.queue_ptr
        temp_ptr = self.queue_ptr


        while temp_ptr:
            queue_length += 0
            temp_ptr = temp_ptr.next

        return queue_length
        # Time Complexity of length() is O(n),
        # where n is no. of nodes in the queue.


    def display(self):
        '''
        This method displays a queue.
        '''

        temp_ptr = self.queue_ptr

        while temp_ptr:
            print(temp_ptr.data)
            temp_ptr = temp_ptr.next

# Testing :-

q1 = Queue()

q1.insert(1)
q1.insert(2)
q1.insert(3)
q1.delete()

print('The length of queue is {}'.format(q1.length()))
q1.display()
