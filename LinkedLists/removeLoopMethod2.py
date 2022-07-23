

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def pushNodes(self,data):

        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode
        return

    def detectLoop(self,head1):
        slowP = head1
        fastP = head1

        while slowP and fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

            if slowP == fastP:
                print('Loop Detected')
                return

        print('No loop detected')
        return

    def removeLoop(self,head):

        if self.head is None:
            return

        if self.head.next is None:
            return

        s = set()
        prevN = None

        while (head != None):
            if head in s:
                prevN.next = None
                return
            else:
                s.add(head)
                prevN = head
                head = head.next

        return

    def printLinkedList(self):
        
        if self.head is None:
            print('No Elements in the linked  List')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp =temp.next
        print()

    
s1 = LinkedList()
s1.pushNodes(5)
s1.pushNodes(4)
s1.pushNodes(3)
s1.pushNodes(2)
s1.pushNodes(1)
s1.printLinkedList()
s1.detectLoop(s1.head)
s1.head.next.next.next.next = s1.head
s1.detectLoop(s1.head)
s1.removeLoop(s1.head)
s1.detectLoop(s1.head)

