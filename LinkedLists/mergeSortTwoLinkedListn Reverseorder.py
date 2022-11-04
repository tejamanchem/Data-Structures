class Node:

    def __init__(self,data):
        self.data = data
        self.next =  None

class LinkedList:

    def __init__(self):
        self.head = None

    def appendNodes(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next = newNode

        return

    def printLinkedList(self):

        if self.head is None:
            print('No Elements in the linkedList')
            return

        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next

        print()

    def SortedMerge(self,a,b):

        if a is None and b is None:
            return

        if b is None:
            return a
        if a is None:
            return b
        res = None
        while a is not None and b is not None:

            if a.data <= b.data:

                temp = a.next

                a.next = res

                res = a

                a = temp

            else:

                temp = b.next

                b.next = res 

                res = b

                b = temp

        while a!=None:

            temp = a.next

            a.next = res

            res = a

            a = temp


        while b!= None:

            temp =b.next
            b.next = res
            res =b
            b= temp

        return res



m1 = LinkedList()
m1.appendNodes(5)
m1.appendNodes(10)
m1.appendNodes(15)
m1.printLinkedList()

m2 =LinkedList()
m2.appendNodes(2)
m2.appendNodes(3)
m2.appendNodes(20)
m2.printLinkedList()

m2.head = m2.SortedMerge(m1.head,m2.head)
m2.printLinkedList()




