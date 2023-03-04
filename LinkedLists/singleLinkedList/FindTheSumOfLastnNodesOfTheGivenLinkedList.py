class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):
        
        if self.head is None:
            self.head = Node(data)
            return
        
        newNode = Node(data=data)

        temp = self.head

        newNode.next = temp
        self.head = newNode
        return
    
    def printLinkedList(self):

        if self.head is None:
            print('No elements in the linked list')
            return
        temp = self.head
        while temp!= None:
            if(temp.next != None):
                print(temp.data,end='->')
            else:
                print(temp.data,end='')
            temp = temp.next
        print()

    def sumOfLastnNumbers_utils(self,head,n):
        global sum
        
        if n <=0:

            return
        
        sum = 0
        self.sumOfLastNNumbers(head)
        return sum
    
        

    def sumOfLastNNumbers(self,head):

        global sum
        global n
        
        if head ==None:
            return
        
        self.sumOfLastNNumbers(head.next)

        if n >0:

            sum = sum  + head.data

            n = n-1



    def sumLastOfNumbersIteration(self,head,n):

        global sum
        if (n <= 0):
            return 0
        
        st = []
        sum =0

        while head !=None:
            st.append(head.data)
            head = head.next

        for i in range(-1,-(n+1),-1):
            sum =  sum + st[i]

        return sum


l1 = LinkedList()
l1.pushNodes(5)
l1.pushNodes(4)
l1.pushNodes(3)
l1.pushNodes(2)
l1.pushNodes(1)
l1.printLinkedList()

n = int(input())

# print(l1.sumOfLastnNumbers_utils(l1.head,n))

print(l1.sumLastOfNumbersIteration(l1.head,n))

        


    
