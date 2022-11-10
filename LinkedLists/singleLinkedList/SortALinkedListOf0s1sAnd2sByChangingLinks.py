class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def pushNode(self,data):
        
        if self.head is None:
            self.head = Node(data)
            return

        newNode = Node(data)

        temp=self.head 
        while temp.next!=None:
            temp=temp.next
        temp.next = newNode
        return

    def printLinkedList(self):
        if self.head is None:
            print('No Elemnts in the linked list')

            return
        temp = self.head
        while temp:
            if temp.next != None:
                print(temp.data,end='->')
            else:
                print(temp.data,end='')
            temp = temp.next
        print()
        return
    def sort012(self,head2):
        if head2 == None or head2.next is None:
            return

        zeroD = Node(0)
        oneD = Node(0)
        twoD = Node(0)

        zero = zeroD
        one = oneD
        two =twoD

        curr = head2
        while curr:
            if curr.data  ==0 :
                zero.next = curr
                zero = zero.next
                curr =curr.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
                curr=curr.next
            else :
                two.next =curr
                two = two.next
                curr=curr.next

        zero.next = (oneD.next) if (oneD.next ) \
                            else (twoD.next)

        one.next = two.next
        two.next = None

        head2 = zeroD.next

        return head2


linkedList1= LinkedList()
linkedList1.pushNode(1)
linkedList1.pushNode(2)
linkedList1.pushNode(0)
linkedList1.pushNode(1)
linkedList1.pushNode(2)
linkedList1.pushNode(0)
linkedList1.printLinkedList()
linkedList1.sort012(linkedList1.head)
# linkedList1.printLinkedList()