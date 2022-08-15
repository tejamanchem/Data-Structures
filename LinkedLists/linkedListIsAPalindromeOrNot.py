
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
            print('No elemenst in the linked list')
            return

        temp=self.head 
        while temp:
            print(temp.data,end=' ')
            temp=temp.next

        print()

    def isPalindrome(self,head1):

        if head1 is None:
            return
        l=[]
        r=[]
        temp=head1
        while temp:
            l.append(str(temp.data))
            temp=temp.next
        
        for i in range(-1,-len(l)-1,-1):
            r.append(l[i])

        joinL = int(''.join(l))
        joinR = int(''.join(r))

        if joinL == joinR:
            print('Palindrome')
        else:
            print('Not a palindrome')


p1 = LinkedList()
p1.appendNodes(1)
p1.appendNodes(2)
p1.appendNodes(1)
p1.printLinkedList()
p1.isPalindrome(p1.head)

p2=LinkedList()
p2.appendNodes(1)
p2.appendNodes(2)
p2.appendNodes(3)
p2.appendNodes(4)
p2.appendNodes(5)
p2.printLinkedList()
p2.isPalindrome(p2.head)

        