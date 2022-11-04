
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def appendNode(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp =temp.next

        temp.next = newNode


    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return

        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp =temp.next

        print()

    def isPalindrome(self,head1):

        if head1 is None:
            return

        l=[]
        l2=[]
        temp = head1
        while temp:
            l.append(str(temp.data))
            temp= temp.next

        for i in range(-1,-len(l)-1,-1):
            l2.append(l[i])

        if (int(''.join(l)) == int(''.join(l2))):
            print('palindrome')
        else:
            print('Not Palindrome')


p1 = LinkedList()
p1.appendNode(1)
p1.appendNode(2)
p1.appendNode(1)
p1.appendNode(3)
p1.printLinkedList()
p1.isPalindrome(p1.head)
