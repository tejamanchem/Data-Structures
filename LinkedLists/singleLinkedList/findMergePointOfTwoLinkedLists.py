

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList1:

    def __init__(self):
        self.head = None

    def appendNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    def printLinkedList(self):

        if self.head is None:
            print('no elements in the linked list')
            return
        
        temp = self.head 

        while temp:
            print(temp.data,end='->')
            temp = temp.next

        print('')

    

    def getMergeNode(self,head1,head2):

        def getCountOfList(listParam1):
            n=0
            while listParam1.next:
                listParam1 = listParam1.next
                n+=1

            return n

        def getNode(d,nodeList1,nodeList2):

            for i in range(d):
                nodeList1 = nodeList1.next

            while nodeList1 and nodeList2:

                if nodeList1 == nodeList2:
                    return nodeList1.data
                else:
                    nodeList1 = nodeList1.next
                    nodeList2 = nodeList2.next

            return None

        c1 = getCountOfList(head1)
        c2 = getCountOfList(head2)
            
        if c1>c2:
            return getNode(c1-c2,head1,head2)

        else:
            return getNode(c2-c1,head2,head1)

    def sortedMerge(self,data1,data2):
        result = None

        
        if data1 is None:
            return data2
        if data2 is None:
            return data1

        if data1.data <= data2.data:
            result = data1
            result.next = self.sortedMerge(data1.next,data2)

        else:
            result = data2
            result.next = self.sortedMerge(data2.next,data1)

        return result
        
        
    def mergeSort(self,h):

        if h is None or h.next is None:
            return h

        middleNode = self.getMiddle(h)
        nextMiddle = middleNode.next
        middleNode.next = None

        left = self.mergeSort(h)
        right = self.mergeSort(nextMiddle)

        sortedMergeList =self.sortedMerge(left,right)

        return sortedMergeList
    def getMiddle(self,head1):
        
        if head1 is None:
            return head1

        slow = head1
        fast = head1

        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

def mergeLinkedList(headA,headB):

    dummyNode = Node(0)

    tail = dummyNode

    while True:


        if headA is None:
            tail.next = headB
            break
        
        if headB is None:
            tail.next = headA
            break
            	
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        tail = tail.next

    return dummyNode.next

    

l1 = LinkedList1()
l1.appendNode(4)
l1.appendNode(1)
l1.appendNode(3)
l1.appendNode(2)

l2 = LinkedList1()
l2.appendNode(9)
l2.appendNode(6)
l2.appendNode(7)
l2.appendNode(8)

print('The Linked Lists are')
l1.printLinkedList()
l2.printLinkedList()


l1.head = l1.mergeSort(l1.head)
l2.head = l2.mergeSort(l2.head)

print('After applying Merge Sort')
l1.printLinkedList()
l2.printLinkedList()

print('After Merging two linked lists')
l1.head = mergeLinkedList(l1.head,l2.head)
l1.printLinkedList()

print('Node that merged two linked lists is')
c=l1.getMergeNode(l1.head,l2.head)
print('The Merged Node is',c)


