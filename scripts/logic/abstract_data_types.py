from collections import deque


# ? Deque ---------------------------------------------------------------------------------------------------------------------
''' Is an ordered collection of items similar to the queue.
    It has two ends, a front and a rear, and the items remain positioned in the collection.
    New items can be added at either the front or the rear. Likewise, existing items can be removed from either end.
    In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.
'''
test_deque = deque()


# ? Stack ---------------------------------------------------------------------------------------------------------------------
''' Is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.
    The base of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack the longest.
'''


class StackADT:
    '''
    LIFO (Last In First Out) pattern.
    when we pushed an item onto the stack, then pushed another, the original item got buried deeper and deeper.
    '''
    def __init__(self) -> None:
        self.data = []


    def push(self, element) -> None:
        '''Add an element to the top of the stack.'''
        self.data.append(element)


    def pop(self) -> object or None:
        '''Remove and return the element from the top of the stack.'''
        raise IndexError('Stack is empty') if self.is_empty() else self.data.pop()


    def peek(self) -> object or None:
        '''Return (but do not remove) the element at the top of'''
        raise IndexError('Stack is empty') if self.is_empty() else self.data[-1]


    def is_empty(self ) -> bool:
        '''Return True if the stack is empty.'''
        return len(self.data) == 0


    def size(self):
        '''Return the number of elements in the stack.'''
        return len(self.data)
 
 
class Queue:
    '''
    FIFO (First In First Out) pattern.
    When we enqueue an item, it gets added to the end of the queue.
    When we dequeue an item, it gets removed from the front of the queue.
    '''
    def __init__(self) -> None:
        self.data = []


    def enqueue(self, e) -> None:
        '''Add element e to the back of the queue.'''
        self.data.insert(0, e)


    def dequeue(self) -> object or None:
        '''Remove and return the first element of the queue. Raise exception if the queue is empty.'''
        raise IndexError('Queue is empty') if self.is_empty() else self.data.pop()


    def peek(self) -> object or None:
        '''Return (but do not remove) the first element of the queue. Raise exception if the queue is empty.'''
        raise IndexError('Queue is empty') if self.is_empty() else self.data[-1]


    def is_empty(self):
        '''Return True if the queue is empty.'''
        return len(self.data) == 0


    def size(self):
        '''Return the number of elements in the queue.'''
        return len(self.data)        


# ? Graph ---------------------------------------------------------------------------------------------------------------------
# A Graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.
#   Adjacency Matrix: A two-dimensional array where the rows represent source vertices and the columns represent destination vertices
#   Adjacency List: A dictionary where the keys are the vertices and the values are lists of vertices that are connected to the key


class Vertex:
    '''
    A vertex is a fundamental part of a graph.
    A vertex may be connected to other vertices via edges.
    '''
    def __init__(self, key) -> None:
        self.id = key
        self.connected_to = {}  # Dictionary of connected vertices and weights


class Graph:
    '''
    A graph is a collection of nodes (vertices) and edges.
    Each node is connected to zero or more other nodes via edges.
    '''
    def __init__(self) -> None:
        self.vert_list = {}
        self.num_vertices = 0

    
    def add_vertex(self, key) -> Vertex:
        '''Add a vertex to the graph.'''
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex


    def get_vertex(self, key) -> object or None:
        '''Return the vertex if it exists.'''
        return self.vert_list[key] if key in self.vert_list else None


    def __contains__(self, key) -> bool:
        '''Return True if the vertex exists.'''
        return key in self.vert_list

    
    def add_edge(self, f, t, cost=0) -> None:
        '''Add an edge to the graph.'''
        if f not in self.vert_list: self.add_vertex(f)
        if t not in self.vert_list: self.add_vertex(t)
        self.vert_list[f].connected_to[self.vert_list[t]] = cost

    
    def get_vertices(self) -> object:
        '''Return a list of all the vertices in the graph.'''
        return self.vert_list.keys()

    
    def __iter__(self) -> object:
        '''Return an iterator of all the vertices in the graph.'''
        return iter(self.vert_list.values())


# ? Heap ----------------------------------------------------------------------------------------------------------------------
import heapq  # min heap
'''
A heap is a specialized tree-based data structure that satisfies the heap property.
If A is a parent node of B then the key (the value) of node A is ordered with respect to the key of node B with the same ordering applying across the heap.
    node: i
    parent: (i-1)//2
    left child: 2*i + 1
    right child: 2*i + 2
'''
random_list = [5, 7, 9, 1, 3]

heapq.heapify(random_list)
# heapq.heappush(heap, item) - push the value item onto the heap, maintaining the heap invariant
# heapq.heappop(heap) - pop and return the smallest item from the heap, maintaining the heap invariant
# heapq.heappushpop(heap, item) - push item on the heap, then pop and return the smallest item from the heap
# heapq.merge(*iterables, key=None, reverse=False) - merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values
# heapq.nlargest(n, iterable, key=None) - return a list with the n largest elements from the dataset defined by iterable
# heapq.nsmallest(n, iterable, key=None) - return a list with the n smallest elements from the dataset defined by iterable
# heapq.replace(heap, item) - pop and return the smallest item from the heap, and also push the new item
# heapq.heapreplace(heap, item) - pop and return the smallest item from the heap, and also push the new item; the heap size is unchanged

print(random_list)  # [1, 3, 9, 7, 5]
