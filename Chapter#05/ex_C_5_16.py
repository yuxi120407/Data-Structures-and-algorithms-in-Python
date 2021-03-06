import ctypes # provides low-level arrays
from time import time

class DynamicArray:
    """ A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not -self._n <= k < self._n:
            raise IndexError('invalid index')
        if k >= 0:
            return self._A[k] # retrieve from array
        else:
            return self._A[self._n + k]
    

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1
        

    def _resize(self, c): # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A = B # use the bigger array
        self._capacity = c
            
    def _make_array(self, c): # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)( ) # see ctypes documentation

    def __str__(self):
        string_rep = '['
        for i in range(len(self)):
            if i == len(self) - 1:
                string_rep = string_rep + str(self._A[i]) + ']'
            else:
                string_rep = string_rep + str(self._A[i]) + ', '
        return string_rep
    
    def insert(self, k, value):
        B = self._A
        """ Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity: # not enough room
            """Resize internal array to capacity c."""
            B = self._make_array(2*self._capacity) # new (bigger) array
            # Copy elements in B upto index k-1
            for j in range(k):
                B[j] = self._A[j]
            
            self._capacity = 2*self._capacity
            
        for j in range(self._n, k, -1): # shift rightmost first
            B[j] = self._A[j-1]
            
        B[k] = value # store newest element
        self._A = B 
        self._n += 1
        
    def pop(self):
        self._n -= 1
        if self._n < self._capacity // 4:
            B = self._make_array(self._capacity // 2)
            self._capacity = self._capacity // 2
            for i in range(self._n):
                B[i] = self._A[i]
            self._A = B
            
        
if __name__ == '__main__':
    
    arr = DynamicArray()
    t = time()
    n = 100
    for i in range(n):
        arr.append(i)
    for i in range(n):
        arr.pop()
    for i in range(n):
        arr.pop()
    print('For {} appends and pops, the average time take is {}'.format(n ,1000000 * (time() - t) / n ))

    arr = DynamicArray()
    t = time()
    n = 1000
    for i in range(n):
        arr.append(i)
    for i in range(n):
        arr.pop()
    for i in range(n):
        arr.pop()
    print('For {} appends and pops, the average time take is {}'.format(n ,1000000 * (time() - t) / n ))

    arr = DynamicArray()
    t = time()
    n = 10000
    for i in range(n):
        arr.append(i)
    for i in range(n):
        arr.pop()
    for i in range(n):
        arr.pop()
    print('For {} appends and pops, the average time take is {}'.format(n ,1000000 * (time() - t) / n ))

    arr = DynamicArray()
    t = time()
    n = 100000
    for i in range(n):
        arr.append(i)
    for i in range(n):
        arr.pop()
    for i in range(n):
        arr.pop()
    print('For {} appends and pops, the average time take is {}'.format(n ,1000000 * (time() - t) / n ))

    arr = DynamicArray()
    t = time()
    n = 1000000
    for i in range(n):
        arr.append(i)
    for i in range(n):
        arr.pop()
    for i in range(n):
        arr.pop()
    print('For {} appends and pops, the average time take is {}'.format(n ,1000000 * (time() - t) / n ))

