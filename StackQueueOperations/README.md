# STACK AND QUEUE OPERATIONS

# Stack:
    A Stack is a LIFO (Last In First Out) data structure. The last element that is placed in a stack is the first element that can be removed. Elements can be inserted and deleted only from one side of the list, called the top.

    The insertion of an element into stack is called pushing. Deletion of an element from the stack is called popping. In stacks, The last element in a list is tracked with a pointer called top.


    Visualizing a Stack:
        Popping an element from a stack will take O(1) time complexity. Popping the last element in a stack will take O(n).

# Queue:
    A Queue is a FIFO (First In First Out) data structure. The first element that is placed in a queue is the first one out. Elements can be inserted only from one side of the list called rear, and the elements can be deleted only from the other side called the front.Think of queues like a queue of people waiting for something. The first person to queue up is the first person served.

    The insertion of an element in a queue is called an enqueue operation and deleting an element is called a dequeue operation. For queues, two pointers are maintained;

    Front pointer: points to the element which was inserted at the first and still present in the list.
    Rear pointer: points to the element inserted last.

    Visualizing a Queue:
        Dequeuing the first element takes O(1) time complexity.

# Why are Stacks and Queues Useful?
    Stacks and Queues are commonly used when implementing Breadth-First-Search (BFS) or Depth-First-Search (DFS) for trees and graphs. Queues are commonly used for BFS and Stacks for DFS.

# Stack and Queue Implementation
    Stacks and Queues often have language specific syntax. In Python, lists are usually used to represent stacks. For Queues, there is a collection called deque.

    Python’s deque objects are implemented as doubly-linked lists which gives them O(1) time complexity for enqueuing and dequeuing elements, but O(n) time complexity for randomly accessing elements in the middle of the queue.

    Because deques support adding and removing elements from either end equally well, you can actually use them for both queues and stacks.

    