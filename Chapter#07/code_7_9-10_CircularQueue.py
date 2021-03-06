class Empty(Exception):
    """ Error attempting to access element from empty container.
        Note that Empty is a subclass of python's builtin Exception class"""
    pass

class CircularQueue:
    """ This class implements Queue using singly linked list as an Adapter Pattern.

        Methods to implement for realizing Stack.
        i)  enqueue(e)
        ii) dequeue()

        Accessor methods.
        i)    first ~ return top element
        ii)   is_empty ~ returns True if the stack is empty.
        iii)  len ~ returns length of the Stack.

    """
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    ######### Methods for CircularQueue.

    def __init__(self):
        # we just need a single pointer that points to tail
        self._size = 0
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queueu is Empty')
        return self._tail._next._element

    def dequeue(self):
        # raise exception in the Queue is empty
        if self.is_empty():
            raise Empty('Queueu is Empty')
        
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
            

        # Update the current size
        self._size -= 1
        
        return old_head._element
    
    def enqueue(self, e):
        # Create node to be enqueued from the tail.
        new_node = self._Node(e, None)
        # _next of the Current tail point to the head.
        if self.is_empty():
            # If the queue is currently empty.
            # tail and head both should be new node. 
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
            
##        current_head = self._tail._next
##        # Since new_node would become the tail, its _next should point to the head.
##        new_node._next = current_head
##        # _next of The current tail should point the new_node.
##        self._tail._next = new_node
        # Update the current tail.
        self._tail = new_node
        # Update the current size
        self._size += 1
        

    def rotate(self):
        # This function makes the current head as the new tail.
        current_head = self._tail._next
        self._tail = current_head
        
        
        
        pass
    

if __name__ == '__main__':
    D = CircularQueue()

    D.enqueue(1)
    D.enqueue(2)
    D.enqueue(3)
    D.enqueue(4)
    D.enqueue(5)
    D.enqueue(6)
    D.enqueue(7)
    D.enqueue(8)
    D.rotate()
    
    node = D._tail#.#_next #()
    while True:
        print(node._element)
        node = node._next
        if node is D._tail:
            break;
    
    
