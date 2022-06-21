# Heap Data Structure
    A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:

1. Introduction to Heap:
    Heap is a tree-based data structure, and a complete binary tree is used for the creation and implementation of a heap.

2. Properties of a Heap:
    Heap is a complete binary tree.
    The root node is located in H[0].
    H[(i-1)/2] returns the parent node.
    H[(2*i)+1] returns the left child node.
    H[(2*i)+2] returns the right child node.
3. Types of Heap:
    Mainly there are two types of Heap namely:

    Max-Heap: A type of heap where the value of the parent node’s values is always greater than its children. This property must be recursively true for all sub-trees in that Binary Tree. The root node consists of the highest value of the heap.

    Min-Heap: A type of heap where the value of the parent node’s values is always lesser than its children. This property must be recursively true for all subtrees in that Binary Tree. The root node consists of the minimum value of the heap.

4. Insertion in a Heap

The insertion into a heap is an easy process. While inserting new elements into heap we need to maintain the heap property. The following is the algorithm for insertion:
Size of the heap must be increased by 1 to accommodate the new element.
Insert the element at the end of the heap, so that the resulting heap so formed, is a complete binary tree.
Compare the value of the element with its parent and swap if the value of the parent is less than the element in case of Max Heap. Value of the parent is more than the element in case of Min Heap.
Continue comparing and swapping until the above condition fails.

5. Deletion from a Heap
The standard protocol that has to be followed while deleting elements from heap is that the element present in the root node can only be deleted.
We must shift the entire tree upwards.
Delete the root node from the tree and copy the last element of the heap to the root.
Compare the current root node with its children and if: Root is greater than any of its children, replace the root with least value of the children in case of Min Heap. Root is lesser than any of its children , replace the root with the greatest value of the children in case of Max Heap.
Continue comparing and swapping until the above condition fails.

6. Heap Sort:
The technique followed in heap sort is deletion of elements in a heap.
In case of Max Heap, the deleted nodes will be of decreasing order as discussed above, therefore the resultant array so formed will have elements in decreasing order.
In case of Min Heap, the deleted nodes will be of increasing order as discussed above, therefore the resultant array so formed will have elements in increasing order.

# HASH DATA STRUCTURE

# Hashing Techniques:
    Hashing is a technique or process of mapping keys, values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used

    Types of Hash Function
        Ideal Hash Function: h(x) = x where x is the element to be mapped.
        Standard Modulus Function: h(x) = x%10 where x is the element to be mapped.
        Custom Random Function: h(x) = <DEFINE_YOUR_FUNCTION>

    What are Collisions?
        A state in a hash table when more than one key is mapped at a specific index. A hash table allows to store only one element per index. A newly inserted key mapped to an already occupied index results in a collision.

    Resolve collisions in Hashing:
        There are two methods to resolve collisions while mapping elements into a hash table. They are:

1. Open Hashing:
    To resolve collisions, the computer might use extra storage space along with the hash table size. It uses an array of linked-lists to resolve collisions.   
    In open hashing the element to be mapped is not stored in a hash table, rather it’s stored in a linked list external to the hash table memory. The word open refers to freedom of mapping values in an external data structure without using the hash memory table.
    Open hashing uses a technique of chaining to resolve collisions. All key-value pairs mapping to the same index will be stored in the linked list of that index.

    Ex- Consider the following elements:

    9, 24, 37, 58, 99, 114, 109, 64, 88
    Hash Function: h(x) = x%10.
    Function Values:
    h(9) = 9%10 = 9

    h(24) = 24 %10 = 4

    h(37) = 37%10 = 7

    h(99) = 99%10 =9

    h(58) = 58%10=8

    h(114) = 114 %10 =4

    h(109) = 109%10=9

    h(64) = 64 % 10 =4

    h(88) = 88 %10 =8

2. Closed Hashing:

    Linear Probing:
        Consider an example: 36, 20, 25, 43, 65, 74, 33, 87

    Modified Hash Function:
        Initially we use the standard modulus function to insert or map values into the hash table.
        When a collision occurs while mapping in the table we use the modified hash function iteratively until an empty index or slot is found.
        h’(x) = [h(x) + f(i)] %10 where f(i) = i; i = 0, 1, 2, 3, 4, 5…
        Hash Functional Values: 36, 20, 25, 43, 65, 74, 33, 99

        h’(36)=6

        h’(20)=0

        h’(25)=5

        h’(43)=3

        h’(65)=5 (C)

        h’(74)=4

        h’(33)=3(C) h’(87)=[C]


2. Quadratic Probing:

    Consider an example:
    36, 20, 25, 43, 65, 74, 33,99

    Modified Hash Function:

        Initially we use the standard modulus function to insert or map values into the hash table.
        When a collision occurs while mapping in the table we use the modified hash function iteratively until an empty index or slot is found.
        h’(x) = [h(x) + f(i)] %10 where f(i) = i²; i = 0, 1, 2, 3, 4, 5…
    Hash Functional Values:

    h’(36)= 6

    h’(20)= 0

    h’(25)= 5

    h’(43)= 3

    h’(65)= 9 (C)

    h’(74)= 4

    h’(33)= 7(C) h’(99) = 1 (C)

3. Double Hashing:

    Consider an example:

    5, 25, 15, 35,95

    Modified Hash Function:

        Initially we use the standard modulus function to insert or map values into the hash table.
        When a collision occurs while mapping in the table we use the modified hash function iteratively until an empty index or slot is found.
        h1(x) = x % 10
        h2(x) = R — ( x % R) where R = closest prime number less than size of hash table.
        h’(x) = [h1(x) + i*h2(x)] %10 where f(i) = i; i = 0, 1, 2, 3, 4, 5…
        Hash Functional Values:

        h’(5)=5

        h’(25)=8

        h’(15)=1

        h’(35)=2

        h’(95)=4
