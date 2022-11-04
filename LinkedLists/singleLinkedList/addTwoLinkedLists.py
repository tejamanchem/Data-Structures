
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
        last = self.head 

        while last.next:
            last = last.next

        last.next = newNode

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
            temp = temp.next

        print('')

    def addingLinkedList(self,list1,list2):
        
        if list1 and list2 is None:
            return
        elif list1 is None:
            result1 = self.adding(list2)
            return result1
        elif list2 is None:
            result2 = self.adding(list1)
            return result2
        else:
            result1 = self.adding(list1)
            result2= self.adding(list2)
            finalResult = result1+result2
            return finalResult

    def adding(self,list3):

        l=[]
        headOList= list3
        while headOList:
            l.append(str(headOList.data))
            headOList = headOList.next
        
        joinedResult = ''.join(l)
        returnResult = int(joinedResult)
        return returnResult

listObj = LinkedList()
listObj.pushNode(1)
listObj.appendNode(2)
listObj.appendNode(3)

listObj1 = LinkedList()
listObj1.appendNode(4)
listObj1.appendNode(5)
listObj1.appendNode(6)

print('linked list is')
listObj.printLinkedList()
listObj1.printLinkedList()


listObj2 = listObj.addingLinkedList(listObj.head,listObj1.head)
print('adding linked list is',listObj2)

