
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

    
class LinkedList:

    def __init__(self):
        self.head = None

    def pushNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

    def printLinkedList(self):

        if self.head is None:
            print('linked list is empty')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next

        print('')

    def detectLoop(self):

        temp =self.head
        detect = self.head
        while temp and detect and temp.next:
            detect = detect.next
            temp = temp.next.next

            if temp == detect:
                print('loop detected')
                return

        print('no loop detected')
        return

    def detectAndRemoveLoop(self):
        slowP = self.head 
        fastP =self.head 

        while slowP and fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

            if slowP == fastP:
                self.removeLoop(slowP)
                return 1
        return 0
    def removeLoop(self,loopHead):

        ptr1 = loopHead
        ptr2 = loopHead
        
        k=1
        while(ptr1.next !=ptr2):
            ptr1 =ptr1.next
            k+=1

        ptr1 = self.head
        ptr2 = self.head

        for i in range(k):
            ptr2 = ptr2.next


        while (ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr2.next != ptr1:
            ptr2 = ptr2.next

        ptr2.next = None

        
li = LinkedList()
li.pushNode(10)
li.pushNode(4)
li.pushNode(15)
li.pushNode(20)
li.pushNode(50)
li.pushNode(60)
li.printLinkedList()
li.detectLoop()
print(li.head.next.next.next.next.next.data)
li.head.next.next.next.next.next = li.head.next.next.next
li.printLinkedList()
li.detectLoop()
li.detectAndRemoveLoop()
li.detectLoop()

