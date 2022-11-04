class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None

class LinkedLists:

    def __init__(self):
        self.head = None

    def pushNodes(self,data):

        newNode = Node(data=data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode
        return

    def printLinkedList(self):
        if self.head is None:
            print('No elements in tye linked lists')
            return

        temp= self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()


class Solution:

    def CountNodes(self,a,b):

        count=0

        while a != None and b !=  None:
            if a.data == b.data:
                count = count+1
            else:
                break
            a=a.next
            b=b.next

        return count

    def lengthOfPalindrome(self,head):

        result =0
        prev = None
        current = head

        while current != None:

            newNode = current.next
            current.next = prev

            result = max(result,2 * self.CountNodes(prev,newNode) +1)

            result = max(result,2 * self.CountNodes(current,newNode))

            prev = current
            current = newNode

        return result


l1 = LinkedLists()
l1.pushNodes(24)
l1.pushNodes(12 )
l1.pushNodes( 2 )
l1.pushNodes(3)
l1.pushNodes( 7 )
l1.pushNodes( 3)
l1.pushNodes(2)
l1.printLinkedList()
l2 = Solution()
result =l2.lengthOfPalindrome(l1.head)
print(result)
l3 = LinkedLists()
l3.pushNodes(3)
l3.pushNodes(1)
l3.pushNodes(3)
result1 = l2.lengthOfPalindrome(l3.head)
print(result1)
