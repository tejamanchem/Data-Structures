class Node:

    def __init__(self,data):
        self.data=data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        if self.head is None:
            self.head = Node(data)
            return
        newNode = Node(data)

        temp = self.head
        while temp.next !=None:
            temp=temp.next
        temp.next = newNode
        return
    def printLinkedList(self):
        if self.head is None:
            print('No elements in the linked list')
            return
        twmp=self.head
        while twmp:
            if(twmp.next!=None):
                print(twmp.data,end='->')
            else:
                print(twmp.data,end='')
            twmp = twmp.next
        print()
        return
    
    def multiplyLinkedList(self,list1,list2):
        if list1 and list2 is None:
            return
        
        num1=0
        num2=0

        head1 = list1.head
        head2 = list2.head

        while (head1!=None or head2!=None):

            if head1 != None:
                num1 = (num1 * 10)+head1.data
                # print(num1)
                head1 = head1.next

            if head2 != None:
                num2 = (num2 * 10)+head2.data
               # j print(num2)
                head2 = head2.next
        return num1*num2


linkedList = LinkedList() 
linkedList.pushNodes(9)
linkedList.pushNodes(4)
linkedList.pushNodes(6)

linkedList2 = LinkedList()
linkedList2.pushNodes(8)
linkedList2.pushNodes(4)

linkedList.printLinkedList()
linkedList2.printLinkedList()

linkedList3= LinkedList()

print(linkedList3.multiplyLinkedList(linkedList,linkedList2))